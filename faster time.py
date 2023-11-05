# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:47:52 2021

@author: Duela
"""

from skyfield.api import EarthSatellite, Topos, load
import skyfield.api
import numpy as np
import time

# Orbit propagation parameters, for 5760 orbit positions over time
SIM_TIME = 1.6*60.*60. # in seconds
TIME_STEP = 1. # in seconds

start_propagation = time.time()
##### Load TLE
ts = load.timescale()
stations_url = 'A_GNSS_2020_10_07.txt'
satellites = load.tle(stations_url,reload=False,)
flock_2k_keys = [k for k in satellites.keys() if "FLOCK 2K" in str(k)]
flock_2k_keys.sort()

for satkey in flock_2k_keys[0:15]:
    cubesat = satellites[satkey]

    ##### Build time array
    cubesat_tle_epoch = cubesat.epoch.utc_datetime()
    seconds = cubesat_tle_epoch.second + np.arange(0, SIM_TIME, TIME_STEP) # 
    time_array = ts.utc(year = cubesat_tle_epoch.year, month = cubesat_tle_epoch.month, day = cubesat_tle_epoch.day, 
                        hour = cubesat_tle_epoch.hour, minute = cubesat_tle_epoch.minute, second = seconds)
    #####

    ##### Perform EarthSatellite.at() orbit propagation
    cubesat_propagated = cubesat.at(time_array)
    #####

    ##### Get GCRS Position in km
    position_gcrs = cubesat_propagated.position.km
    #####

    ##### Get GCRS Velocity in km/s
    velocity_gcrs = cubesat_propagated.velocity.km_per_s
    #####

stop_propagation = time.time()
print("--- Skyfield Orbit Propagation ---\n"\
      "Total Computation Time (for 15 sats, {0} sequential orbit positions): {1} seconds"
      .format(int(SIM_TIME/TIME_STEP), stop_propagation-start_propagation))