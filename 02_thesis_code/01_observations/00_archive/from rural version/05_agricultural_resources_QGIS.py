#extract agricultural resource data
##climate: aridity index (growing days?)
##slope/topography

##ARIDITY INDEX
radius_list = [3,4,5,6,7]
direct_list = []
for i in radius_list:
    #grid cells with observations 
    inp = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/02_extracted_grid/grid_extract_" + str(i) + ".shp")
    #visible lights
    out = str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/03_AR/aridity_index/aridity_index_" + str(i) + ".csv")
    pref = None 
    processing.run("native:zonalstatisticsfb", \
    {'INPUT':inp,\
    'INPUT_RASTER':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/03_AR/Climate/Aridity_Index/06_aridity_index_irr_adj_clip.tif', \
    'RASTER_BAND':1,\
    'COLUMN_PREFIX': pref,'STATISTICS':[0,1,2],\
    'OUTPUT': out})
    
    

#topography 
##ruggedness 
for i in radius_list:
    #grid cells with observations 
    inp = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/02_extracted_grid/grid_extract_" + str(i) + ".shp")
    #visible lights
    out = str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/03_AR/ruggedness/ruggedness_" + str(i) + ".csv")
    pref = None 
    processing.run("native:zonalstatisticsfb", \
    {'INPUT':inp,\
    'INPUT_RASTER':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/03_AR/Topography/ruggedness.tif', \
    'RASTER_BAND':1,\
    'COLUMN_PREFIX': pref,'STATISTICS':[0,1,2],\
    'OUTPUT': out})

    