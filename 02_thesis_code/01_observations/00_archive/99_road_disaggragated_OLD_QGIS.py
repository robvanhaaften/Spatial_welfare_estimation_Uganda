from pathlib import Path
from pathlib import PureWindowsPath
import pandas as pd

#split roads by catagroy for all of uganda, makes seperate shapefiles and stores them
def road_split_uganda():
    processing.run("native:splitvectorlayer", \
    {'INPUT':'C:/Users/Rob/Desktop/GIS_thesis/01_thesis_data/01_input/02_road/hotosm_uga_roads_lines_shp/hotosm_uga_roads_lines.shp',\
    'FIELD':'highway','FILE_TYPE':1,\
    'OUTPUT':'C:\\Users\\Rob\\Dropbox\\My PC (DESKTOP-DP7OCOF)\\Desktop\\GIS_thesis\\01_thesis_data\\02_temp\\02_road\\roads_split\\uganda_total'})

#creates zonal statistics for each of the 30 road type and 5 grid size saves them to CSV
def create_zonal_statistics():
    #generate a list of all the road type file paths created in road_split_uganda()
    shp_folder_road = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\uganda_total').rglob('*.shp')
    files_road = [x for x in shp_folder_road]

    #generate a list of all the grid size file paths created in XXXX
    shp_folder_grid = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\06_observations\02_extracted_grid').rglob('*.shp')
    files_grid = [x for x in shp_folder_grid]

    #count for numbering variables in file (REMOVE?)
    count = 0
    for grid in files_grid:
        folder = PureWindowsPath(grid).name.split('.')[0]
        count += 1
        for road_type in files_road:
            file = PureWindowsPath(road_type).name.split('.')[0]
            print(count)
            print(folder)
            print(file)
            processing.run("native:sumlinelengths", \
            {'POLYGONS':str(grid),\
            'LINES':str(road_type),\
            'LEN_FIELD':str(str(file) + str(count) + 'length'),\
            'COUNT_FIELD':str(str(file) + str(count) + 'count'),\
            'OUTPUT':str(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\%s\%s.csv' %(folder, file))})


#merge files for each grid size 
#####REPLACE THE ENDLESS DIRECTORIES WITH THIS SHIT!!!!###
base_dir = r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats'

def merge_zonal_stats(): 
    #generates a list of folder names to go through (the 3 to 7 KM grids)
    zonal_stats_folders = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\\').rglob("")
    grid_folders = [x for x in zonal_stats_folders]
    for directory in grid_folders[1:]:
        # generates a list of csv files for each folder (the 30 roadtypes)
        folder = PureWindowsPath(directory).name
        zonal_stats_csv = Path(str(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\\' + str(folder))).rglob('*.csv')
        csv_list = [str(x) for x in zonal_stats_csv]
     
        #makes a merged csv file for each grid size 
        processing.run("native:mergevectorlayers", 
        {'LAYERS':csv_list,\
        'CRS':None, \
        'OUTPUT':str(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\\' + str(folder) + '_merged.csv')})



def merge_roads_dhs():
    #clean merged files and merge into one single csv with dhs data 
    road_csvs_obj = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\\').rglob("*merged.csv")
    road_csvs = [str(x) for x in road_csvs_obj]

    #import dhs data 
    dhs = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\04_DHS\ug_dhs_wi.csv")
    dhs_roads = dhs.copy() 

    #merge all with the dhs file sand keep only length, drop the "unmaintained" variable, has no observations and gives errors 
    for i in road_csvs:
        road = pd.read_csv(i)
        #make wide by grouping by cluster taking the max values (that is only the observations) 
        road = road.groupby(by = "DHSCLUST").max()
        #drop everything but length and 
        road = road[road.columns[(road.columns.str.endswith('length'))]]
        #drop everything iwth only 0 values
        road = road.loc[:, (road**2).sum() != 0]
        #drop unmaintained column 
        road = road[road.columns[(~road.columns.str.contains("maintained"))]]
        print(road.describe())
        dhs_roads = dhs_roads.merge(road, left_on = "cluster", right_index = True)
        
    
    #save merged file 
    dhs_roads.to_csv(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\dhs_roads_split.csv')


#1 split the road data per roadtupe for each gridsize 
#road_split_uganda()

#2 create zonal statistics for each grid size and road type
#create_zonal_statistics()

#3 merge all the excel sheets per grid size 
#merge_zonal_stats()

#4 Clean and merge the road files with dhs and save to csv
#merge_roads_dhs()







