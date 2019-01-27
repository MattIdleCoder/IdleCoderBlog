#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This little program tests the forward transverse Mercator equations for
converting traditional latitude and longitude coords to their tranverse Mercator
equivalent. The result is a plot of the transformed positions of several cities,
islands and oceans.
 
Equations are from: en.wikipedia.org/wiki/
Transverse_Mercator_projection#Direct_transformation_formulae
 
Created on 5 May 2018
@author: matta_idlecoder@protonmail.com
"""
 
import numpy as np
import matplotlib.pyplot as plt
from collections import namedtuple
import timeit
 
timing = True
 
 
def new_y_coord(lat, longtde):
    """Converts a lat, longitude location to a new transformed longitude
    """
    lat_in_rads = lat / 180 * np.pi
    long_in_rads = longtde / 180 * np.pi
    new_y_rad = 0.5 * np.log((1 + (np.sin(long_in_rads) * np.cos(lat_in_rads)))
                            (1 - (np.sin(long_in_rads) * np.cos(lat_in_rads))))
    new_y_deg = new_y_rad * 180 / np.pi
    return new_y_deg
 
 
def new_x_coord(lat, longtde):
    """Converts a lat, longitude location to a new transformed latitude
    """
    lat_in_rads = lat / 180 * np.pi
    long_in_rads = longtde / 180 * np.pi
    new_x_rad = -(np.arctan((np.tan(lat_in_rads)) / (np.cos(long_in_rads))))
    new_x_deg = new_x_rad  * 180 / np.pi
 
    """this code fixes the arctan problem of mapping only back to 
    -90 < arctan > 90. It does this by checking the position on the world map.
    """
    if longtde < -90 or longtde > 90:
        if lat > 0:
            new_x_deg -= 180
        elif lat < 0:
            new_x_deg += 180
    return new_x_deg
 
 
def plot_meridians():
    """Plots the transformed lines of latitude and longitude
    """
    plt.figure(figsize=(15, 12), dpi=80)
 
    plt.xlim(-180.0, 180.0)
    plt.xticks(range(-90, 91, 90))
 
    plt.ylim(-175.0, 175.0)
    plt.yticks(range(-180, 181, 180))
 
    plt.xlabel('Equator')
    plt.ylabel('0 = International Dateline & \nGreenwich Meridian')
    plt.title("Transverse Mercator Projection with Pole at 0'N, 90'W")
 
    long_x, long_y = [], []
    # plot the transformed lines of longitude:
    for longitude in range(-180, 181, 10):  # for ea vertical line of longitude
        for latitude in range(-90, 91, 1):  # print every point
            if not latitude and abs(longitude) == 90:  # don't div by 0 at poles
                continue  # don't calculate the point
            x = round(new_x_coord(latitude, longitude), 2)
            y = round(new_y_coord(latitude, longitude), 2)
            long_x.append(x)
            long_y.append(y)
    plt.plot(long_x, long_y, 'g.', linewidth=0.5, label='Lines of Longitude')
 
    Lat_x, Lat_y = [], []
    # plot the transformed lines of latitude:
    for latitude in range(-90, 91, 10):  # for each horizontal line of latitude
        for longitude in range(-180, 181, 1):  # print every point
            if not latitude and abs(longitude) == 90:  # don't div by 0 at poles
                continue  # don't calculate the point
            x = round(new_x_coord(latitude, longitude), 2)
            y = round(new_y_coord(latitude, longitude), 2)
            Lat_x.append(x)
            Lat_y.append(y)
 
    plt.plot(Lat_x, Lat_y, 'b--', linewidth=0.5, label='Lines of Latitude')
    plt.legend(loc='upper right')
    return
 
 
def plot_places():
    """Plots major world cities and places after a Shifted Mercator Transform
    """
 
    City = namedtuple('City', 'name lat_long text_coords colour')
    Ocean = namedtuple('Ocean', 'name lat_long text_coords')
 
    Places = [
        City(name='North Pole', lat_long=(90, 0), text_coords=(-130, 10),
             colour='yellow'),
        City(name='South Pole', lat_long=(-90, 0), text_coords=(110, -5),
             colour='yellow'),
        City(name='Greenwich meridian', lat_long=(5,0), text_coords=(-18, -15),
             colour='green'),
        City(name='Edinburgh', lat_long=(56, -4), text_coords=(-45, -5),
             colour='blue'),
        City(name='Sydney', lat_long=(-33, 152), text_coords=(130, 40),
             colour='red'),
        City(name='Rio', lat_long=(-22, -43), text_coords=(0, -40),
             colour='black'),
        City(name='Singapore', lat_long=(2, 104), text_coords=(-170, 90),
             colour='black'),
        City(name='S India', lat_long=(7, 77), text_coords=(-57, 97),
             colour='orange'),
        City(name='Quito', lat_long=(-2, -78), text_coords=(-20, -130),
             colour='blue'),
        City(name='Buenos Aires', lat_long=(-35, -56), text_coords=(40, -70),
             colour='brown'),
        City(name='Tierra del Fuego', lat_long=(-55, -65), text_coords=(100, -40),
             colour='yellow'),
        City(name='Caracas', lat_long=(10, -67), text_coords=(-50, -70),
             colour='orange'),
        City(name='Mexico City', lat_long=(19, -98), text_coords=(-145, -100),
             colour='red'),
        City(name='Los Angeles', lat_long=(33, -118), text_coords=(-145, -75),
             colour='black'),
        City(name='New York', lat_long=(42, -73), text_coords=(-55, -45),
             colour='violet'),
        City(name='Tokyo', lat_long=(36, 140), text_coords=(-160, 45),
             colour='green'),
        City(name='Auckland', lat_long=(-37, 175), text_coords=(150, -5),
             colour='red'),
        City(name='Moscow', lat_long=(56, 37), text_coords=(-52, 25),
             colour='red'),
        City(name='Cape Town', lat_long=(-34, 19), text_coords=(0, 10),
             colour='brown'),
        City(name='Cairo', lat_long=(30, 32), text_coords=(-25, 30),
             colour='red'),
        City(name='Baghdad', lat_long=(33, 45), text_coords=(-30, 50),
             colour='blue'),
        City(name='Bangkok', lat_long=(14, 101), text_coords=(-115, 120),
             colour='yellow'),
        City(name='Beijing', lat_long=(41, 115), text_coords=(-100, 60),
             colour='orange'),
        City(name='Kerguelen Is (Fr)', lat_long=(-49, 70), text_coords=(63, 63),
             colour='black'),
        City(name='SGeorgia', lat_long=(-55, -35), text_coords=(32, -11),
             colour='yellow')]
 
    Oceans = [
        Ocean(name='Indian Ocean', lat_long=(-20, 80), text_coords=(40, 135)),
        Ocean(name='N Pacific Ocean', lat_long=(30, -170),
              text_coords=(-175, -38)),
        Ocean(name='S Pacific Ocean', lat_long=(-30, 140),
              text_coords=(-129, -80))]
 
    for place in Places:
        city_x, city_y = new_x_coord(*place.lat_long), \
                         new_y_coord(*place.lat_long)
        plt.annotate(place.name, xy=(city_x, city_y), xytext=place.text_coords,
                     arrowprops=dict(facecolor=place.colour, shrink=0.05))
 
    for watery_place in Oceans:
        ocean_x, ocean_y = new_x_coord(*watery_place.lat_long), \
                           new_y_coord(*watery_place.lat_long)
        plt.annotate(watery_place.name, xy=(ocean_x, ocean_y),
                     xytext=watery_place.text_coords)
    return
 
 
if __name__ == '__main__':
    if timing:
        zerotime = timeit.default_timer()
 
    plot_meridians()
    plot_places()
    plt.show()
 
    if timing:
        now = timeit.default_timer()
        print('That took', round(now - zerotime, 2), 'seconds.\n')

