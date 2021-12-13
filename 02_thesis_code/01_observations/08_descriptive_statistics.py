# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:03:02 2021
@author: Rob

make descriptive statistics tables

1. Descirptive statistics of the DHS(2016 and 2018-19), NTL, total road length and aridity index 

2. Make kernel density plots 

3. Descriptive statistics for roads differentiated by type 

"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")



### 1. DHS, NTL, total road length, aridity index ###
# Import data from analysis 1 (not standardized)
data = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\01_analysis1\data_analysis1.csv")

# dhs mis survey data for verification of model 
dhs_2018 = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\05_dhs\ug_dhs_mis_wi.csv")

# Clean 
# Keep data: cluster, wealth index, and 3km observations 
data = data[data.columns[data.columns.str.contains('3') | data.columns.str.contains('wi')]]

# Rename data columns
data.rename(columns={
    
    "wi"                : "Wealth index DHS standard 2016", 
    "ntl_mean_3"        : "Nighttime light", 
    "road_length_3"     : "Road length", 
    "aridity_mean_3"    : "Adjusted aridity index"
    
    }, inplace=True)

# Rename dhs 2018 
dhs_2018.rename(columns ={
    
    "wi"                : "Wealth index DHS MIS 2018-19"
    
    }, inplace=True)

# Make dictionary to store statistics 
stats ={}
stats["Wealth index DHS MIS 2018-19"] = [round(np.mean(dhs_2018["Wealth index DHS MIS 2018-19"]))]
stats["Wealth index DHS MIS 2018-19"] += [round(np.std(dhs_2018["Wealth index DHS MIS 2018-19"]))]
stats["Wealth index DHS MIS 2018-19"] += [round(np.min(dhs_2018["Wealth index DHS MIS 2018-19"]))]
stats["Wealth index DHS MIS 2018-19"] += [round(np.max(dhs_2018["Wealth index DHS MIS 2018-19"]))]
stats["Wealth index DHS MIS 2018-19"] += [len(dhs_2018["Wealth index DHS MIS 2018-19"])]

# Loop over variable names and add the mean, standard deviation, min value, max value and number of observations to the dictionary 
for i in list(data):
    stats[i] = [round(np.mean(data[i]), 2)]
    stats[i] += [round(np.std(data[i]), 2)]
    stats[i] += [round(np.min(data[i]), 2)]
    stats[i] += [round(np.max(data[i]), 2)]
    stats[i] += [len(data[i])]

# Make a dataframe from the dictionary 
stats = pd.DataFrame.from_dict(stats, orient ="index", columns =  ["Mean", "SD", "Min","Max", "N"])
# Save dataframe to csv 
stats.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\tables\descriptives.csv")


# 2. Make kernel density plots 
for count, var in enumerate(list(data)):
    plt.show()
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data[var])
    plt.savefig(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\plots\Figure%s.pdf" %str(count+1))


# 3. Descriptive statistics for roads differentiated by type 
# Import road types data 
data_road_types = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\dhs_roads_split.csv")

# Keep only the relevant data: cluster, wealth index, and 3km observations 
data_road_types = data_road_types[data_road_types.columns[data_road_types.columns.str.contains('3')]]

# Rename columns
data_road_types.rename(columns = {
    
    "highway_bridleway3length"          : "Bridleway", 
    "highway_construction3length"       : "Construction", 
    "highway_crossing3length"           : "Crossing", 
    "highway_cycleway3length"           : "Cycleway", 
    "highway_footway3length"            : "Footway", 
    "highway_living_street3length"      : "Living street", 
    "highway_motorway3length"           : "Motorway", 
    "highway_motorway_link3length"      : "Motorway link", 
    "highway_path3length"               : "Path", 
    "highway_pedestrian3length"         : "Pedestrian", 
    "highway_primary3length"            : "Primary", 
    "highway_primary_link3length"       : "Primary link", 
    "highway_proposed3length"           : "Proposed", 
    "highway_residential3length"        : "Residential", 
    "highway_road3length"               : "Road", 
    "highway_secondary3length"          : "Secondary", 
    "highway_secondary_link3length"     : "Secondary link", 
    "highway_service3length"            : "Service", 
    "highway_steps3length"              : "Steps",
    "highway_tertiary3length"           : "Tertiary", 
    "highway_tertiary_link3length"      : "Tertiary link", 
    "highway_trunk3length"              : "Trunk", 
    "highway_trunk_link3length"         : "Trunk link", 
    "highway_unclassified3length"       : "Unclassified"
    
    }, inplace=True)

# Make dictionary to store statistics 
stats_road_types ={}

# Loop over variable names 
# Add the mean, standard deviation, min value, max value and number of observations to the dictionary 
for i in list(data_road_types):
    stats_road_types[i] = [round(np.mean(data_road_types[i]), 2)]
    stats_road_types[i] += [round(np.std(data_road_types[i]), 2)]
    stats_road_types[i] += [round(np.min(data_road_types[i]), 2)]
    stats_road_types[i] += [round(np.max(data_road_types[i]), 2)]
    stats_road_types[i] += [len(data_road_types[i])]
    
    
# Make a dataframe from the dictionary 
stats_road_types = pd.DataFrame.from_dict(stats_road_types, orient ="index", columns =  ["Mean", "SD", "Min","Max", "N"])
# Save dataframe to csv 
stats_road_types.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\tables\descriptives_road_types.csv")


