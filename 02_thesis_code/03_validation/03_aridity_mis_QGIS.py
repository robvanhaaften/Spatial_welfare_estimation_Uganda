"""
Created on Fri Oct 15 2021
@author: Rob van Haaften

Calculates the average adjusted aridity index for each hexagon 

"""

# Input grid cells DHS MIS
inp = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/04_dhs_mis_grid/dhs_grid_mis.shp")
# Directory to save results 
out = str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/04_aridity/02_observations/aridity_mis.csv")

# Calculates average adjusted aridity index for each hexagon with DHS MIS observations 
processing.run("native:zonalstatisticsfb", \
{'INPUT':inp,\
'INPUT_RASTER':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/04_aridity/01_input/aridity_index_adj.tif', \
'RASTER_BAND':1,\
'COLUMN_PREFIX': None,'STATISTICS':[2],\
'OUTPUT': out})


