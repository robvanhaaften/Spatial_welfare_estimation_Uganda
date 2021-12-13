
"""
Created on Fri Oct 15
@author: Rob van Haaften

Makes the hexagonal grids which are used to extract the observations

The script is devided into three functions that do the following: 

1. Create a hexagonal grid covering Uganda for hexagons with 5 diameter sizes, 3 to 7 kilometers 

2. Clip the above created grids by the administrative boundaries of Uganda 

3. Extracts the grid cells that contain observations from the DHS survey


"""

# 1. Create a hexagonal grid covering Uganda for hexagon diamters 3 to 7 kilometers 
def create_grid():
    # List of grid sizes in degrees. Corresponds to [3, 4, 5, 6, 7] in kilometers at the ugandan latitude.
    grid_sizes = [0.027, 0.036, 0.045, 0.054, 0.063]

    # Base directory to save the grids 
    directory = 'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/01_complete_grid/grid_'

    # Directory document suffix 
    km = 3 

    # Loop over the list of grid sizes and generate a grid covering uganda 
    for i in grid_sizes: 
        out = str(directory + str(km) + ".shp") 
        processing.run("native:creategrid", \
        {'TYPE':4,\
        'EXTENT':'29.572161695,35.001053632,-1.481474356,4.231366981 [EPSG:4326]',\
        'HSPACING':i,'VSPACING':i,'HOVERLAY':0,'VOVERLAY':0,\
        'CRS':QgsCoordinateReferenceSystem('EPSG:4326'),\
        'OUTPUT':out})
        # add 1 for next grid size
        km += 1


# 2. Clip the above created grids by the administrative boundaries of Uganda to shave off the edges
def extract_uganda():
    # This join function joins the grid file witht the Ugandan administrative boundaries shapefile to discard all the cells completely outside the boundaries 
    for i in [*range(3,8,1)]: 
        # Join with uganda boundaries and extract all placed within the Ugandan country level administrative boundary 
        processing.run("native:joinattributesbylocation", \
        {'INPUT': str(directory + str(i) + ".shp"),\
        'JOIN':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/01_input/05_uganda/adminstrative_boundaries/gadm36_UGA_0.shp',\
        'PREDICATE':[0,4],'JOIN_FIELDS':[],'METHOD':0,'DISCARD_NONMATCHING':True,\
        'PREFIX':'','OUTPUT': str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/02_uganda_grid/uganda_grid_' + str(i)+ ".shp")})\


# 3. Extract the grid cells that contain observations from the DHS survey 
def extract_dhs():
    for i in [*range(3,8,1)]:
        processing.run("native:joinattributesbylocation", \
        {'INPUT': str(directory + str(i) + ".shp"),\
        'JOIN':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/01_input/04_DHS/Uganda/Uganda_2016_GEO_SHP/UGGE7AFL.shp',\
        'PREDICATE':[1],\
        'JOIN_FIELDS':['DHSCLUST','DHSREGCO'],\
        'METHOD':0,'DISCARD_NONMATCHING':True,'PREFIX':'',\
        'OUTPUT':str('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/01_observations/03_dhs_grid/dhs_grid_' + str(i) +".shp")})

# un-comment to run the seperarate functions 

#create_grid()

#extract_uganda()

#extract_dhs()









