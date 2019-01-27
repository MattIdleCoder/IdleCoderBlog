#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{0}: redraws a given standard Mercator projection world map with the poles
moved to 90E & 90W at the equator. Runs on multiple CPU cores. Will run on any
image format or size of input map. Assumes maps stop at 85º N/S.

Equations are explained at:
en.wikipedia.org/wiki/Transverse_Mercator_projection#Inverse_transformation_formulae

The following flags are optional:
    -i input_map
        The name of the input map filename. No extension required: program will
        auto-detect the image type. With no -i flag, it will look for an
        input file called WorldMap.png

    -o output_map
        The name you want to give your transformed output map. With no -o flag,
        it will output to a file called ShiftedWorldMap.jpg
        Requires an image type suffix, which can be any of the standard image
        file types (.gif .bmp .jpg .jpeg .ppm .png .tif or .tiff).
        Defaults to a .jpg output if none given.

    -c NumCores
        The number of cores you want to run the program on.
        On this computer you can set it to a number between 1 and {1}.
        Default setting is 2.

    -n LinesPerCore
        The number of lines you want each CPU to process at a time.
        Must be between 1 and 10. Default is 2.

    -d
        don't display the input and output maps on the console

    -h
        Prints this __doc__ string

    -t
        Time the program execution

Example command line:
    python3 {0} -i myMap.png -o myNewMap.png -c4 -n4 -t

Or, if you cd to the same folder and make this file executable using chmod +x:
    ./{0} -i myMap.png -o myNewMap.png -c4 -n4 -t

Created 20 Dec, 2018
@author: matta_idlecoder@protonmail.com
"""

from PIL import Image
import numpy as np
import sys
import getopt
import timeit
from concurrent import futures
import os

timing_it = False
displaying_images = True
profiling = False


def inv_merc_lat(translat_in_rads, translong_in_rads):
    """Calculates orig transverse mercator latitude for a given image coord
    """
    orig_lat_rad = -np.arcsin((np.sin(translong_in_rads)) / (np.cosh(translat_in_rads)))
    return orig_lat_rad


def inv_merc_long(trans_lat_rads, trans_long_rads):
    """Calculates the orig transverse mercator longitude for a given image coord
    """
    orig_long_rads = np.arctan(np.sinh(trans_lat_rads) / np.cos(trans_long_rads))
    if (trans_long_rads > np.pi/2) or (trans_long_rads < -np.pi / 2):
        if trans_lat_rads >= 0:
            orig_long_rads += np.pi
        elif trans_lat_rads < 0:
            orig_long_rads -= np.pi
    return orig_long_rads


def inv_transform_pixel(x_pix_num, x_max, y_max, transformed_lat):
    """Calculates the corresponding pixel position from the input image

    :param x_pix_num: pixel number on the output image
    :param x_max: x dimension of the input and output images
    :param y_max: y dimension of the input and output images
    :param transformed_lat: radians of longitude of output image line
    :return: the input image coordinate to use for this the output image
    coordinate given by x_coord, map_line_num (in inv_transform_line)
    """
    trans_longitude = round((float(x_pix_num) / x_max * 2 * np.pi) - np.pi, 2)
    orig_latitude = round(inv_merc_lat(transformed_lat, trans_longitude), 3)
    orig_longitude = round(inv_merc_long(transformed_lat, trans_longitude), 3)

    original_x = int((orig_longitude + np.pi) / (2 * np.pi) * x_max)
    original_y = int((orig_latitude - np.pi / 2) / (-np.pi) * y_max)

    # fixes potential rounding and index errors:
    original_x -= 1 if original_x == x_max else 0
    original_y -= 1 if original_y == y_max else 0

    return original_y, original_x


def inv_transform_line(map_line_num, x_max, y_max):
    """Finds the transformed image pixel pos, for each pixel in the given line

    :param map_line_num: The line number being transformed.
    :param x_max: The width of the input image, in pixels.
    :param y_max: The height of the input image, in lines.
    :return: (1) the map_line_num that was sent to it. This is a modification to
            the single threaded version, to tag the returned data, so that we
            know which line it is. The order that the ProcessPoolExecutor
            returns the processed lines is not guaranteed.
            (2) line_pixel_mapping, a mapping for every pixel on the line, to
            the corresponding pixel coordinates before the transformation. This is
            not an image line, but rather a pixel-to-pixel mapping that will
            then be unpacked to construct the transformed output image of pixel
            values, line by line, from the input image.
    """
    # image may be 1000s of pixels wide. Thus > 8 bit & < 64 bit, and unsigned:
    line_pixel_mapping = np.zeros((x_max, 2), dtype=np.uint16)

    # mapping of line # to a decimal between 0 and 1.0:
    y_norm = float(map_line_num+1) / y_max

    # maps lines top to bottom to +175 -> -175 deg (in radians)
    # line number has now been converted into radians of longitude:
    trans_lat = round((y_norm * (-35 * np.pi / 18)) + (17.5 * np.pi / 18), 2)

    # for each pixel coord on the output image line:
    for x_coord in range(x_max):  
        # Map it to a curve on the input image map:
        line_pixel_mapping[x_coord] = inv_transform_pixel(x_coord, x_max, y_max,
                                                          trans_lat)
    # return the mapped line, plus its line number to identify it:
    return map_line_num, line_pixel_mapping


def inv_trans_mult_lines(max_x, max_y, *lines):
    """    Calculates multiple lines at a time

    :param x_max: the x dimension of the image
    :param y_max: the y dimension of the image
    :param lines: list of line numbers
    :return:
    """
    line_pair_res = []
    for line_num in lines:
        line_pair_res.append(inv_transform_line(line_num, max_x, max_y))
    return line_pair_res


def inv_transform_map(map_input_name, map_output_name, workers=2,
                      lines_per_core=2):
    """Builds an output map image from the input image via the inv transform

    :param map_input_name: string
    :param map_output_name: string
    :param workers: number of CPUs to use in parallel
    :param lines_per_core: number of image lines to pass to each CPU
    :return: when complete
    """

    try:
        input_image = Image.open(map_input_name)
        X_PIC_SIZE, Y_PIC_SIZE = input_image.size
        if displaying_images:
            input_image.show()

        map_trimmed = False
        while Y_PIC_SIZE % lines_per_core:  # there will be lines left over
            # trim it a little, so the zip don't run out of lines:
            Y_PIC_SIZE -= 1
            map_trimmed = True

    except FileNotFoundError:
        raise SystemExit("\nInput map {} isn't there. Check the filename is correct.\n".
              format(map_input_name))

    core_plural = "" if workers == 1 else "s"
    line_plural = "" if lines_per_core == 1 else "s"
    trim_string = "" if not map_trimmed else "slightly trimmed "
    print("\nRunning map transform on {} core{}, {} line{} at a time on a {}{}x{} map...".
          format(workers, core_plural, lines_per_core, line_plural, trim_string,
                 X_PIC_SIZE, Y_PIC_SIZE))

    transformed_lines = []
    # essentially, a short list of generators which, once zipped, will create
    # groups of lines to be processeed by each core:
    list_of_ranges = [range(line_number, Y_PIC_SIZE, lines_per_core)
                      for line_number in range(lines_per_core)]

    with futures.ProcessPoolExecutor(workers) as executor:
        result = (executor.submit(inv_trans_mult_lines, X_PIC_SIZE,
                    Y_PIC_SIZE, *lines) for lines in zip(*(list_of_ranges)))

        # save the results, in whatever order they are completed:
        for future in futures.as_completed(result):
            res = future.result()
            for res_line in res:
                    transformed_lines.append((res_line[0], res_line[1]))

    # Extract and sort 2D list of pixel mappings:
    trans_image_data = np.zeros((Y_PIC_SIZE, X_PIC_SIZE, 2), dtype=np.uint16)
    for trans_line in transformed_lines:
        trans_image_data[trans_line[0]] = trans_line[1]

    # Create transformed image data:
    output_image_data = np.zeros((Y_PIC_SIZE, X_PIC_SIZE, 3), dtype=np.uint8)
    for line in range(Y_PIC_SIZE):
        for pixel in range(X_PIC_SIZE):
            new_pix_line, new_pix_x = trans_image_data[line][pixel]
            # The [:3] is to read only the RGB input image data if it's RGBA:
            output_image_data[line][pixel] = input_image.getpixel(
                (int(new_pix_x), int(new_pix_line)))[:3]

    # Create transformed image:
    output_image = Image.fromarray(output_image_data, 'RGB')

    if displaying_images:
        output_image.show()
    if not map_output_name:
        map_output_name = "ShiftedPoleMap.png"
    output_image.save(map_output_name)
    return


def usage(prog_name):
    """Prints a short command line guide, using whatever filename this prog has.
    """
    print("""\nUsage: from the command line type:
    {} [-i input_filename] [-o output_filename.ext] [-c NumCores] [-n LinesPerCore] [-dht]

    If you don't want to use flags, give your input file the name WorldMap.png
    and your output filename the name will be given the name ShiftedWorldMap.jpg
    
    NumCores is the number of cores/CPUs/processors you want to use. 
    On this computer you can set it to a number between 1 and {} (defaults to 2).
    
    LinesPerCore is the number of lines you want each core to process at a time.
    Must be between 1 and 10. Default is 2.
    
    Use the -d flag to suppress displaying the input and output images.
    
    Use the -t flag to time your map transformation.

    Use the -h flag for a detailed flag listing.

    """.format(prog_name, os.cpu_count()))
    return


def main(argv):

    global displaying_images, timing_it

    # Just in case your IDE hands you the whole path as sys.argv[0]:
    prog_name = os.path.split(sys.argv[0])[-1]

    input_map_name = 'WorldMap.png'
    output_map_name = 'ShiftedPoleMap.jpg'

    cores_in_use = 2
    AVAIL_CORES = os.cpu_count()
    MAX_LINES_PER_CORE = 10
    lines_per_calc = 2

    try:
        opts, args = getopt.getopt(argv, "c:n:i:o:dht")

    except getopt.GetoptError as err:
        print("\n", str(err))
        usage(prog_name)
        raise SystemExit()

    for opt, arg in opts:
        if opt == '-d':
            displaying_images = False
        elif opt == '-i':
            input_map_name = arg
        elif opt == '-o':
            output_map_name = arg
            ext = os.path.splitext(output_map_name)[-1].lower()
            if ext not in ".gif .bmp .jpg .jpeg .ppm .png .tif .tiff".split():
                output_map_name += '.jpg'  # smallest file format
                print ('Unknown output file extension. Creating a JPEG file.')
        elif opt == '-n':
            try:
                if 1 <= int(arg) <= MAX_LINES_PER_CORE:
                    lines_per_calc = int(arg)
                else:
                    raise SystemExit("\nCommand line error: number of image lines per core must be between 1 and {}.\n".
                          format(MAX_LINES_PER_CORE))
            except ValueError:
                raise SystemExit("\nCommand line type error: -n flag needs a integer.\n")

        elif opt == '-c':
            try:
                if 1 <= int(arg) <= AVAIL_CORES:
                    cores_in_use = int(arg)
                else:
                    raise SystemExit("\nCommand line core number error: NumCores must be between 1 and {}.\n".
                          format(AVAIL_CORES))
            except ValueError:
                print("\nCommand line type error: -c flag needs an integer.\n".
                      format(AVAIL_CORES))
                raise SystemExit("Check your command line.")
        elif opt == '-h':
            print("\n", __doc__.format(prog_name, AVAIL_CORES))
            raise SystemExit()
        elif opt == '-t':
            timing_it = True
        else:
            assert False, "unhandled option"

    if timing_it:
        start = timeit.default_timer()

    inv_transform_map(input_map_name, output_map_name, workers=cores_in_use,
                      lines_per_core=lines_per_calc)

    if timing_it:
        stop = timeit.default_timer()
        print('\nFinished the map transform in', round((stop - start), 2),
              'seconds.\n')
    return


if __name__ == '__main__':
    if profiling:
        import profile
        profile.run('main(sys.argv[1:])')
        
    else:
        main(sys.argv[1:])


        


