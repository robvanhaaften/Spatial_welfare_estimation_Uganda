
import pandas as pd

##make final map
#merge vector results excel sheet with the shapefile layers for the uganda grid 
processing.run("native:mergevectorlayers", \
{'LAYERS':['C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/03_output/map/model_results.csv',\
'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/03_uganda_grid/uganda_grid_7.dbf|layername=uganda_grid_7',\
'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/03_uganda_grid/uganda_grid_7.shx|layername=uganda_grid_7',\
'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/02_temp/06_observations/03_uganda_grid/uganda_grid_7.shp'],\
'CRS':None,'OUTPUT':'C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/03_output/map/model_results_merge.csv'})

#clean the ugly qgis merge
results = pd.read_csv('C:/Users/Rob/Dropbox/My PC (DESKTOP-DP7OCOF)/Desktop/GIS_thesis/01_thesis_data/03_output/map/model_results_merge.csv')
results.groupby("id").max()
print(results.head())



