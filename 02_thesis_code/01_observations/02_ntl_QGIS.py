"""
Created on Fri Oct 15
@author: Rob van Haaften

Generates the ntl observations using the Google Earth Engine (GEE) 

To calculate the mean ntl intensity the dhs_grid files were manualy uploaded to the authors GEE account 

"""

import ee
from ee_plugin import Map
import geemap
import os

# Access the monthly average radiance NTL data from the GEE the year 2016
NTL_data = ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')\
.filterDate('2016-01-01', '2016-12-21')\
.select('avg_rad')

# Takes the mean for 2016
NTL_mean = NTL_data.mean()


# The extracted dhs gridcell shapefiles were uploaded to the authors google earth engine acount's "assets"
# These are now imported as a feature collection 
grid3 = ee.FeatureCollection('users/RobvHaaften/dhs_grid_3');
grid4 = ee.FeatureCollection('users/RobvHaaften/dhs_grid_4');
grid5 = ee.FeatureCollection('users/RobvHaaften/dhs_grid_5');
grid6 = ee.FeatureCollection('users/RobvHaaften/dhs_grid_6');
grid7 = ee.FeatureCollection('users/RobvHaaften/dhs_grid_7');

# Make a list of above grid files 
gridlist = [grid3, grid4, grid5, grid6, grid7]

# Set directory to store the observations
out_dir = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/02_NTL/ntl_observations'

# Loop over the gridlist to calculate means of average radiance for each dhs observation hexagon and for each grid size 
km = 3
for grid in gridlist:
    path_end = 'ntl_' + str(km) + '.csv'
    out_stats_dir = os.path.join(out_dir, path_end)  
    # Calculate zonal statistics mean, scale is in meters 
    geemap.zonal_statistics(NTL_mean, grid, out_stats_dir, statistics_type='MEAN', scale=500)
    # Add 1 for the nexy grid size 
    km += 1



