"""
Created on Fri Oct 15

Calculates the sum of all the road lengths within each hexagon

@author: Rob van Haaften
"""

# loops through grids for the 5 different gridsizes and calculate the road length for all the survey observation cells 
for i in [*range(3,8,1)]:
    out = 'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/03_road/road_aggregate/road_' + str(i) + '.csv'
    processing.run("native:sumlinelengths", \
    {'POLYGONS':str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/03_dhs_grid/dhs_grid_' + str(i) + '.shp'),\
    'LINES':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/01_input/02_road/hotosm_uga_roads_lines_shp/hotosm_uga_roads_lines.shp',\
    'LEN_FIELD':'length','COUNT_FIELD':str('count'),\
    'OUTPUT':out})

