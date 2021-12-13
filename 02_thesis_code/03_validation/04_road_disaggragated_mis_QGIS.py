"""
Created on Fri Oct 15 2021
@author: Rob van Haaften

Calculates the road length for the disaggragated road data at 3-kilometer grid size for all the DHS MIS observations 

1. Calculate the total road length for the different road types at 3-kilometers 

2. Merges the observations with DHS MIS data and saves to csv file 

"""

from pathlib import Path
from pathlib import PureWindowsPath
import pandas as pd



# 1. Calculates the total road length for the different road types 
def create_zonal_statistics():
    # Generate a list of all the road type file paths created in road_split_uganda()
    shp_folder_road = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\uganda_total').rglob('*.shp')
    files_road = [x for x in shp_folder_road]
    
    grid = "C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/04_dhs_mis_grid/dhs_grid_mis.shp"
    for road_type in files_road:
        file = PureWindowsPath(road_type).name.split('.')[0]
        processing.run("native:sumlinelengths", \
        {'POLYGONS':grid,\
        'LINES':str(road_type),\
        'LEN_FIELD':str(str(file) + 'length'),\
        'COUNT_FIELD':str(str(file) + 'count'),\
        'OUTPUT':str(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\zonal_stats\dhs_mis\%s.csv' %(file))})


# Merge the observations 
base_dir = r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\zonal_stats'

def merge_zonal_stats(): 
    # Generate a list of csv files for each folder (the 30 roadtypes)
    zonal_stats_csv = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\zonal_stats\dhs_mis\\').rglob('*.csv')
    csv_list = [str(x) for x in zonal_stats_csv]
    # Make a merged csv file of all the road types 
    processing.run("native:mergevectorlayers", 
    {'LAYERS':csv_list,\
    'CRS':None, \
    'OUTPUT':str(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\zonal_stats\mis_merged.csv')})


# Un-comment to run the funcitons (the first function takes a while to run)
# 1. Calculates the total road length for the different road types at 3-kilometers 
#create_zonal_statistics()

# 2. Merges the observations with DHS MIS data and saves to csv file 
#merge_zonal_stats()







