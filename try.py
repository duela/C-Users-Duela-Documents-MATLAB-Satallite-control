# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:25:29 2021

@author: Duela
"""

from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite, Topos
import skyfield.api
import numpy as np

stations = 'A_GNSS_2020_10_07.txt'
satellites = load.tle_file(stations)
print('Loaded', len(satellites), 'satellites')
by_name = {sat.name: sat for sat in satellites}
satellite = by_name['GPS BIIR-2  (PRN 13)']
print(satellite)
print(stations)
