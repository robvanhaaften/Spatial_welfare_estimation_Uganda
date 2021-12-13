#Load VIIRS Images
import ee
from ee_plugin import Map
import geemap
import os

#get population density 2015
pop_data = ee.ImageCollection("CIESIN/GPWv411/GPW_Population_Density")\
.filterDate('2015-01-01', '2015-05-01');

#add population density layer 
#Map.addLayer(pop_data)

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
out_dir = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/05_population_density'


#loop over list to calculate means of average radiance for each hexagon and each grid size 
#geemap zonal stats tutorial https://tutorials.geemap.org/Analysis/zonal_statistics/
#make a list of grid files 
gridlist = [grid3, grid4, grid5, grid6, grid7]
number = 3
for grid in gridlist:
    path_end = 'pop_' + str(number) + '.csv'
    out_stats_dir = os.path.join(out_dir, path_end)  
    #calculate zonal statistics mean, scale is in meters 
    geemap.zonal_statistics(pop_data, grid, out_stats_dir, statistics_type='MEAN')
    number += 1

