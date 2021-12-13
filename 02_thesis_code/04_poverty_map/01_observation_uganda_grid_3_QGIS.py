


#####NTL#####
#Load VIIRS Images
import ee
from ee_plugin import Map

import geemap
import os
from pathlib import Path
from pathlib import PureWindowsPath
import pandas as pd

#get NTL annual average 2016 
NTL_data = ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMCFG')\
.filterDate('2016-01-01', '2016-12-21')\
.select('avg_rad')
NTL_mean = NTL_data.mean()

#identify grid from google earth engine assets 
grid3 = ee.FeatureCollection('users/RobvHaaften/uganda_grid_3');
#calculate zonal stats for grid 3

#geemap zonal stats tutorial https://tutorials.geemap.org/Analysis/zonal_statistics/
path_out = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/NTL_VIIRS_uganda_2.csv'
#calculate zonal statistics mean, scale is in meters 
geemap.zonal_statistics(NTL_mean, grid3, path_out, statistics_type='MEAN', scale=500)


#####road#####
#creates zonal statistics for each of the 30 road type and 5 grid size saves them to CSV
def create_zonal_statistics():
    #generate a list of all the road type file paths created in road_split_uganda()
    shp_folder_road = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\uganda_total').rglob('*.shp')
    files_road = [x for x in shp_folder_road]

    #input uganda grid
    input_grid = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/03_uganda_grid/uganda_grid_3.shp")
    #count for numbering variables in file (REMOVE?)
    count = 0
    for road_type in files_road:
        file = PureWindowsPath(road_type).name.split('.')[0]
        print(count)
        print(file)
        processing.run("native:sumlinelengths", \
        {'POLYGONS':input_grid,\
        'LINES':str(road_type),\
        'LEN_FIELD':str(str(file) + str(count) + 'length'),\
        'COUNT_FIELD':str(str(file) + str(count) + 'count'),\
        'OUTPUT':str(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats_uganda\%s.csv' %(file))})


#first create the zonal stats 
create_zonal_statistics()

#still got to merge them see 04_roads_split

####aridity####

#grid cells with observations 
input_grid = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/03_uganda_grid/uganda_grid_3.shp")
input_raster = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/03_AR/Climate/Aridity_Index/06_aridity_index_irr_adj_clip.tif")
out_dir = str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/03_AR/aridity_index/aridity_index_uganda_3.csv")
pref = None 
processing.run("native:zonalstatisticsfb", \
{'INPUT':input_grid,\
'INPUT_RASTER':input_raster, \
'RASTER_BAND':1,\
'COLUMN_PREFIX': pref,'STATISTICS':[0,1,2],\
'OUTPUT': out_dir})















