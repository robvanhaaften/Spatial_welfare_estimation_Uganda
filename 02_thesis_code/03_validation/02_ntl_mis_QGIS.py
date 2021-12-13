"""
Created on Fri Oct 15

Generates the ntl observations using the Google Earth Engine (GEE) 

To calculate the average ntl brightness the dhs_grid files were manualy uploaded to the authors GEE account 

@author: Rob van Haaften
"""

import ee
from ee_plugin import Map
import geemap
import os

# Access the monthly average radiance NTL data from the GEE the year 2016
NTL_data = ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')\
.filterDate('2018-01-01', '2019-12-21')\
.select('avg_rad')

# Takes the mean for 2016
NTL_mean = NTL_data.mean()

# The extracted dhs gridcell shapefiles were uploaded to the authors google earth engine acount's "assets"
# These are now imported as a feature collection 
grid = ee.FeatureCollection('users/RobvHaaften/dhs_grid_mis');

# Set a directory to store results 
out_dir = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/02_NTL/ntl_observations/ntl_mis.csv'

# Means of average radiance for each dhs mis observation hexagon 
# Calculate zonal statistics mean
geemap.zonal_statistics(NTL_mean, grid, out_dir, statistics_type='MEAN', scale=500)




