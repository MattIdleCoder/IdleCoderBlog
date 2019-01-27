#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
{0}: redraws a given standard Mercator projection world map with the poles
moved to 90E & 90W at the equator. Uses the concurrent.futures parallel 
processing module to calculate the map transform pixel by pixel.

Equations are explained at:
en.wikipedia.org/wiki/
Transverse_Mercator_projection#Inverse_transformation_formulae

The following flags are optional:
    -i input_map
        The name of the input map filename. No extension required: program will
        auto-detect the image type. With no -i flag, it will look for an
        input file called WorldMap.png

    -o output_map
        The name you want to give your transformed output map. With no -o flag,
        it will output to a file called ShiftedPoleMap.jpg
        Requires an image type suffix, which can be any of the standard image
        file types (.gif .bmp .jpg .jpeg .ppm .png .tif or .tiff).
        Defaults to a .jpg output if none given.

    -d
        don't display maps when running the program

    -h
        Prints this __doc__ string

    -t
        Time the program execution

Example command line:
    python3 ./{0} -i myMap.png -o myNewMap.png -t

Or, if you cd to the same folder and make this file executable:
    ./{0} -i myMap.png -o myNewMap.png -t

Created 15 Dec, 2018
@author: matta_idlecoder@protonmail.com
"""

from PIL import Image
import numpy as np
import sys
import getopt
import timeit
from concurrent import futures
import os

displaying_images = True
timing_it = True

def inv_merc_lat(translat_in_rads, translong_in_rads):
    """Converts a transverse mercator latitude to its original latitude.
    """
    orig_lat_rad = -np.arcsin((np.sin(translong_in_rads)) / (np.cosh(translat_in_rads)))
    return orig_lat_rad


def inv_merc_long(trans_lat_rads, trans_long_rads):
    """Converts a transverse mercator longitude to its original longitude.
    """
    orig_long_rads = np.arctan(np.sinh(trans_lat_rads) / np.cos(trans_long_rads))
    if (trans_long_rads > np.pi / 2) or (trans_long_rads < -np.pi / 2):
        if trans_lat_rads >= 0:
            orig_long_rads += np.pi
        elif trans_lat_rads < 0:
            orig_long_rads -= np.pi
    return orig_long_rads


def inv_transform_pixel(map_line_num, x_pix_num, x_max, y_max, transformed_lat):
    """Calculates the new pixel position in the transformed image
    """
    trans_longitude = round((float(x_pix_num) / x_max * 2 * np.pi) - np.pi, 2)
    orig_latitude = round(inv_merc_lat(transformed_lat, trans_longitude), 3)
    orig_longitude = round(inv_merc_long(transformed_lat, trans_longitude), 3)
    original_x = int((orig_longitude + np.pi) / (2 * np.pi) * x_max)
    original_y = int((orig_latitude - np.pi / 2) / (-np.pi) * y_max)
    # fixes potential rounding and index errors:
    original_x -= 1 if original_x == x_max else 0
    original_y -= 1 if original_y == y_max else 0
    
    return map_line_num, x_pix_num, original_y, original_x


def inv_transform_map(map_input_name, output_map):
    """Builds a new transformed map image line by line, pixel by pixel
    """
    workers = 4
    try:
        input_image = Image.open(map_input_name)
        X_PIC_SIZE, Y_PIC_SIZE = input_image.size
        if displaying_images:
            input_image.show()

    except FileNotFoundError:
        print("\nInput map {} isn't there. Check the filename is correct.\n".
              format(map_input_name))
        sys.exit(2)

    print("\nRunning the map transform...\n")

    X_PIC_SIZE, Y_PIC_SIZE = input_image.size
    pixel_result_list = []

    for map_line in range(Y_PIC_SIZE):  # for each line
        y_norm = float(map_line) / Y_PIC_SIZE
        trans_lat = round(y_norm * (-35 * np.pi / 18) + (17 * np.pi / 18), 2)

        with futures.ProcessPoolExecutor(workers) as executor:
            result = (executor.submit(inv_transform_pixel, map_line, x_coord,
                                      X_PIC_SIZE, Y_PIC_SIZE, trans_lat)
                        for x_coord in range(X_PIC_SIZE))

            # save the results, in whatever order they are completed:
            for future in futures.as_completed(result):
                res = future.result()
                pixel_result_list.append(
                    ([res[0], res[1]], [res[2], res[3]]))

    # Create transformed image data:
    output_image_data = np.zeros((Y_PIC_SIZE, X_PIC_SIZE, 3), dtype=np.uint8)
    for pixel_mapping in sorted(pixel_result_list):
        # The [:3] is to read only the RGB input image data if it's RGBA:
        output_image_data[pixel_mapping[0][0], pixel_mapping[0][1]] = \
                    input_image.getpixel(tuple(pixel_mapping[1][::-1]))[:3]

    # Create transformed image:
    output_image = Image.fromarray(output_image_data, 'RGB')

    if displaying_images:
        output_image.show()
    if not output_map:
        output_map = "ShiftedPoleMap.png"
    output_image.save(output_map)
    return


def usage(prog_name):
    """Prints a short command line guide, using whatever filename this prog has.

    """
    print("""\nUsage: from the command line type:
    {} [-i input_filename] [-o output_filename.ext] [-dht]

    If you don't want to use flags, give your input file the name WorldMap.png
    and your output filename will be given the name ShiftedPoleMap.jpg

    Use the -t flag to time your map transformation.

    Use the -h flag for a detailed flag listing.

    """.format(prog_name))
    return


def main(argv):
    global displaying_images, timing_it

    input_map_name = 'WorldMap.png'
    output_map_name = 'ShiftedPoleMap.jpg'

    try:
        opts, args = getopt.getopt(argv, "i:o:dht")

    except getopt.GetoptError as err:
        print("\n", str(err))
        usage(sys.argv[0])
        sys.exit(2)

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
                print('Unknown output file extension. Creating a JPEG file.')
        elif opt == '-h':
            print("\n", __doc__.format(sys.argv[0][2:]))
            sys.exit(2)
        elif opt == '-t':
            timing_it = True
        else:
            assert False, "unhandled option"

    if timing_it:
        start = timeit.default_timer()

    inv_transform_map(input_map_name, output_map_name)

    if timing_it:
        stop = timeit.default_timer()
        print('\nFinished the map transform in', round((stop - start), 2),
              'seconds.\n')
    return


if __name__ == '__main__':
    main(sys.argv[1:])
