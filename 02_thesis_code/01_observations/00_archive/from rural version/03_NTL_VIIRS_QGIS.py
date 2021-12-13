#Load VIIRS Images
import ee
from ee_plugin import Map
import geemap
import os

#get NTL annual average 2016 
NTL_data = ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')\
.filterDate('2016-01-01', '2016-12-21')\
.select('avg_rad')
NTL_mean = NTL_data.mean()


#clip it for uganda
#countries = ee.FeatureCollection("FAO/GAUL/2015/level0");

#Uganda = countries.filter(ee.Filter.eq('ADM0_NAME', 'Uganda'));
#print(Uganda)


#add NTL layer 
Map.addLayer(NTL_mean)

#grids were uploaded too google earth engine assets
#from shapefiles created in GIS_thesis\02_thesis_code\01_pre-processing\01 and 02
#import grids from google earth engine assets 
grid3 = ee.FeatureCollection('users/RobvHaaften/grid_extract_3');
grid4 = ee.FeatureCollection('users/RobvHaaften/grid_extract_4');
grid5 = ee.FeatureCollection('users/RobvHaaften/grid_extract_5');
grid6 = ee.FeatureCollection('users/RobvHaaften/grid_extract_6');
grid7 = ee.FeatureCollection('users/RobvHaaften/grid_extract_7');

#adding grid to map
#grid3 = grid3.geometry();
#Map.addLayer(grid3)

#calculate zonal stats for each grid 

#Set outdirectory 
out_dir = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/grid_observations_VIIRS'


#loop over list to calculate means of average radiance for each hexagon and each grid size 
#geemap zonal stats tutorial https://tutorials.geemap.org/Analysis/zonal_statistics/
#make a list of grid files 
gridlist = [grid3, grid4, grid5, grid6, grid7]
number = 3
for grid in gridlist:
    path_end = 'NTL_VIIRS_' + str(number) + '.csv'
    out_stats_dir = os.path.join(out_dir, path_end)  
    #calculate zonal statistics mean, scale is in meters 
    geemap.zonal_statistics(NTL_mean, grid, out_stats_dir, statistics_type='MEAN', scale=500)
    number += 1

