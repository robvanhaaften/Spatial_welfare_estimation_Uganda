##Join grid and dhs clusters and extract cells that contain cluster 

grid_list = [ '3.shp', '4.shp', '5.shp', '6.shp', '7.shp']
#get dhs observations and seperate by urban rural 
processing.run("native:splitvectorlayer", \
{'INPUT':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/01_input/04_DHS/Uganda/Uganda_2016_GEO_SHP/UGGE7AFL.shp',\
'FIELD':'URBAN_RURA','FILE_TYPE':0,\
'OUTPUT':'C:\\Users\\Rob\\Dropbox\\My PC (DESKTOP-DP7OCOF)\\Desktop\\GIS_thesis\\01_thesis_data\\02_temp\\04_DHS'})

for i in grid_list:
    processing.run("native:joinattributesbylocation", \
    {'INPUT': str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/01_complete_grid/grid_'+ i),\
    'JOIN':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/04_DHS/URBAN_RURA_R.gpkg',\
    'PREDICATE':[1],\
    'JOIN_FIELDS':['DHSCLUST','DHSREGCO'],\
    'METHOD':0,'DISCARD_NONMATCHING':True,'PREFIX':'',\
    'OUTPUT':str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/02_extracted_grid/grid_extract_' + i)})