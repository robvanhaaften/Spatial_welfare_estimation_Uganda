


km = 3 

for i in [*range(3,8,1)]: 
    #join with uganda boundaries and extract 
    processing.run("native:joinattributesbylocation", \
    {'INPUT': str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/01_complete_grid/grid_'+ str(i) + ".shp"),\
    'JOIN':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/01_input/05_uganda/adminstrative_boundaries/gadm36_UGA_0.shp',\
    'PREDICATE':[0,4],'JOIN_FIELDS':[],'METHOD':0,'DISCARD_NONMATCHING':True,\
    'PREFIX':'','OUTPUT': str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/03_uganda_grid/uganda_grid_' + str(i)+ ".shp")})\
