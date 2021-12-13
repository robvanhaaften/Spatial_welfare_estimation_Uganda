"""
Created on Fri Sep 17 16:43:26 2021

make grids to generate observations 

@author: Rob
"""


#greate the grids for calculating stastics and 

#list of spacing degrees, roughly corresponds to 3 to 7 km in degrees
degree_list = [0.027, 0.036, 0.045, 0.054, 0.063]

#directory base 
directory = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/01_complete_grid/grid_'

#directory document suffix 
km = 3 

#
for i in degree_list: 
    out = str(directory + str(km) + ".shp") 
    processing.run("native:creategrid", \
    {'TYPE':4,\
    'EXTENT':'29.572161695,35.001053632,-1.481474356,4.231366981 [EPSG:4326]',\
    'HSPACING':i,'VSPACING':i,'HOVERLAY':0,'VOVERLAY':0,\
    'CRS':QgsCoordinateReferenceSystem('EPSG:4326'),\
    'OUTPUT':out})
    km += 1


