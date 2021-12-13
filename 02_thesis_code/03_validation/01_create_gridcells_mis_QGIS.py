
"""
Created on Fri Oct 15
@author: Rob van Haaften

Extracts the grid cells that contain observations from the DHS MIS survey

"""

processing.run("native:joinattributesbylocation", \
{'INPUT': r'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/01_complete_grid/grid_3.shp',\
'JOIN':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/01_input/04_DHS/Uganda_2018-19_GEO_SHP/UGGE7IFL.shp',\
'PREDICATE':[1],\
'JOIN_FIELDS':['DHSCLUST','DHSREGCO'],\
'METHOD':0,'DISCARD_NONMATCHING':True,'PREFIX':'',\
'OUTPUT':str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/04_dhs_mis_grid/dhs_grid_mis.shp")})









