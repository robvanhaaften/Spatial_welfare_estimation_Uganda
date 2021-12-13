#generate statistics for sum of lengths of roads (length) and number of roads (count), undiferentiated 

radius_list = [3,4,5,6,7]
direct_list = []
for i in radius_list:
    out = 'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/02_temp/02_road/road_aggregate/road' + str(i) + '.csv'
    processing.run("native:sumlinelengths", \
    {'POLYGONS':str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/02_extracted_grid/grid_extract_' + str(i) + '.shp'),\
    'LINES':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/01_input/02_road/hotosm_uga_roads_lines_shp/hotosm_uga_roads_lines.shp',\
    'LEN_FIELD':str('road'+str(i)+ 'length'),'COUNT_FIELD':str('road' + str(i) + 'count'),\
    'OUTPUT':out})
    direct_list.append(out)
print(direct_list)

#to do
#write directory list to file so dont need to copypaste
#use path instead of directory list?
