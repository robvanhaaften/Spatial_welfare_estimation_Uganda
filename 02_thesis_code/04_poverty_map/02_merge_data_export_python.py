# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:27:29 2021

making the final map 
1. get data for all of Uganda for the 3 kilometer grid and merge on grid id 
2. get coeficients from final model
3. calculate the estimates for complete grid



@author: Rob
"""
import pandas as pd

# 1. get data for all of Uganda for the 3 kilometer grid and merge on grid id 
# merge data for compelte uganda extract for NTL, roads and AR
# import data
ntl = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_NTL\NTL_VIIRS_uganda_3.csv")
ntl = ntl[["id", "mean"]]

aridity = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\04_aridity\02_observations\aridity_index_uganda_3.csv")
aridity = aridity[["id", "_mean"]]

# setting up a dataframe for road types wiht the id's
road_data = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\zonal_stats_uganda_3\highway_bridleway.csv")
ids = road_data[["id"]]
road_data = ids.copy()

# list of road types for model see output from analysis_3
road_vars = [
            'highway_construction',
            'highway_cycleway',
            'highway_footway',
            'highway_living_street',
            'highway_path',
            'highway_pedestrian',
            'highway_primary',
            'highway_residential',
            'highway_road',
            'highway_secondary',
            'highway_steps',
            'highway_trunk',
            'highway_unclassified'
             ]

# get road types and merge 
for i in road_vars:
    direct = str(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\zonal_stats_uganda_3\\" + str(i) +'.csv')
    road_type = pd.read_csv(direct)
    road_data = pd.merge(road_data,road_type, on = "id")

# clean the QGIS mess 
road_data = road_data[[
                        "id",
                        'highway_construction3length',
                         'highway_cycleway3length',
                         'highway_footway3length',
                         'highway_living_street3length',
                         'highway_path3length',
                         'highway_pedestrian3length',
                         'highway_primary3length',
                         'highway_residential3length',
                         'highway_road3length',
                         'highway_secondary3length',
                         'highway_steps3length',
                         'highway_trunk3length',
                         'highway_unclassified3length'
                         ]]

# 2. get coeficients from final model
coeficients = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\03_analysis3\model_coeficients.csv", index_col=0)

# Create new column for each variable multiplied by its coeficient 
ntl["ntl_value"] = ntl["mean"].apply(lambda x: x * coeficients.iloc[1]) 
aridity["aridity_value"] = aridity["_mean"].apply(lambda x: x * coeficients.iloc[2])

# Loop over road variables and multiply them their coeficients
count = 1
for i in road_vars:
    road_data[str(i+"_value")] = road_data.iloc[:,count].apply(lambda x: x * coeficients.iloc[count+2])
    count += 1

# dataframe to merge results 
output = ids.copy()

for i in [ntl, aridity, road_data]:
    output = pd.merge(left = output, right = i, on = "id")

# add intercept 
output["intercept"] =  pd.Series([int(coeficients.iloc[0]) for x in range(len(output.index))])

# clean everything 
output = output[[
                "id", 
                "intercept", 
                "ntl_value", 
                "aridity_value", 
                'highway_construction_value',
                'highway_cycleway_value',
                'highway_footway_value',
                'highway_living_street_value',
                'highway_path_value',
                'highway_pedestrian_value',
                'highway_primary_value',
                'highway_residential_value',
                'highway_road_value',
                'highway_secondary_value',
                'highway_steps_value',
                'highway_trunk_value',
                'highway_unclassified_value'
                ]]

# make result column, sum up everything but the "id" column
output["result"] = output[list(output)[1:len(list(output))]].sum(axis=1)

# export to csv 
output.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\04_verification\dhs_2018-19_estimates.csv")
