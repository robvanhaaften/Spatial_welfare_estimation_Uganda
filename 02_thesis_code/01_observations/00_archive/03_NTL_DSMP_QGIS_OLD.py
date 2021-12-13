#Generate zonal statistics for ntl

radius_list = [3,4,5,6,7]
direct_list = []
for i in radius_list:
    #grid cells with observations 
    inp = str("C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/02_extracted_grid/grid_extract_" + str(i) + ".shp")
    #visible lights
    out = str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/grid_observations/vis" + str(i) + ".csv")
    pref = str("vis" + str(i))
    processing.run("native:zonalstatisticsfb", \
    {'INPUT':inp,\
    'INPUT_RASTER':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/visibleNTL_uganda_clip.tif', \
    'RASTER_BAND':1,\
    'COLUMN_PREFIX': pref,'STATISTICS':[0,1,2],\
    'OUTPUT': out})
    # add directory to list visible 
    direct_list.append(out)
    
    #stable lights
    out = str("C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/grid_observations/stab" + str(i) + ".csv")
    pref = str("stab" + str(i))
    processing.run("native:zonalstatisticsfb", \
    {'INPUT':inp,\
    'INPUT_RASTER':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/stableNTL_uganda_clip.tif', \
    'RASTER_BAND':1,\
    'COLUMN_PREFIX': pref,'STATISTICS':[0,1,2],\
    'OUTPUT': out})
    # add directory to list stable 
    direct_list.append(out)

#to do
#write directory list to file so dont need to copypaste

#merge output
base_directory = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/grid_observations/'
processing.run("native:mergevectorlayers", 
{'LAYERS':[ str(base_directory + 'stab3.csv'),str(base_directory + 'stab4.csv'),\
str(base_directory + 'stab5.csv'),str(base_directory + 'stab6.csv'),str(base_directory + 'stab7.csv'),str(base_directory + 'vis3.csv'),\
str(base_directory + 'vis4.csv'),str(base_directory + 'vis5.csv'),str(base_directory + 'vis6.csv'),str(base_directory + 'vis7.csv')],\
'CRS':None,'OUTPUT':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_NTL/grid_observations/NTL_merged.csv'})