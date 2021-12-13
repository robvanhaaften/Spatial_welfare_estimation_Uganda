# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 18:27:35 2021

Merging DHS, NTL, roads and AR data

To do:
    -add AR data, aridity and topography
    -add population data 
    -write general function for merging... but need consistent                                              inputt for that?

# - directory
# - column names 
# - main differences between google earth engine stuff and own files 


@author: Rob
"""

import pandas as pd

#import DHS rural wealth index data 
dhs = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\04_DHS\ug_dhs_wi.csv")


###NTL###
#make a new DF for merging
dhs_ntl = dhs.copy()

#import NTL VIIRS for each scale and merge with DHS
for i in [*range(3,8,1)]:
    dir = str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\grid_observations_VIIRS\NTL_VIIRS_" + str(i) + ".csv")
    ntl = pd.read_csv(dir)
    ntl = ntl[["DHSCLUST", "mean"]]
    ntl.rename(columns = {"mean":str("ntl_mean_"+str(i)), }, inplace=True)
    dhs_ntl = dhs_ntl.merge(ntl, left_on = "cluster", right_on = "DHSCLUST")


###NTL+ROAD###
#make new DF for merging
dhs_ntl_road = dhs_ntl

#import road for each scale and merge with DHS_NTL DF 
for i in [*range(3,8,1)]:
    dir = str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\road_aggregate\road"+ str(i) +".csv")
    road = pd.read_csv(dir)
    road = road[["DHSCLUST",str("road"+ str(i) + "length")]]
    road.rename(columns = {str("road"+ str(i) + "length"):str("road_length_"+str(i))}, inplace=True)
    dhs_ntl_road = dhs_ntl_road.merge(road, left_on = "cluster", right_on = "DHSCLUST")
    
###NTL+ROAD+ARIDITY###
#make new DF for merging
dhs_ntl_road_aridity = dhs_ntl_road

#import road for each scale and merge with DHS_NTL DF 
vars_aridity = []
for i in [*range(3,8,1)]:
    dir = str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\03_AR\aridity_index\aridity_index_" + str(i) +".csv")
    aridity = pd.read_csv(dir)
    aridity = aridity[["DHSCLUST", "_mean"]]
    aridity.rename(columns = {"_mean":str("aridity_mean_" +str(i))}, inplace=True)
    dhs_ntl_road_aridity = dhs_ntl_road_aridity.merge(aridity, left_on = "cluster", right_on = "DHSCLUST")
    vars_aridity.append(str("aridity_mean_" +str(i)))

###NTL+ROAD+ARIDITY+RUGGED###
dhs_ntl_road_aridity_rugged = dhs_ntl_road_aridity

vars_rugged = []
for i in [*range(3,8,1)]:
    dir = str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\03_AR\ruggedness\ruggedness_" + str(i) +".csv")
    rugged = pd.read_csv(dir)
    rugged = rugged[["DHSCLUST", "_mean"]]
    rugged.rename(columns = {"_mean":str("rugged_mean_" +str(i))}, inplace=True)
    dhs_ntl_road_aridity_rugged = dhs_ntl_road_aridity_rugged.merge(rugged, left_on = "cluster", right_on = "DHSCLUST")
    vars_rugged.append(str("rugged_mean_" +str(i)))


#clean by dropping all the clustter clutter 
dhs_ntl_road_aridity_rugged = dhs_ntl_road_aridity_rugged[["cluster", "quant_sep", "score_sep", "ntl_mean_3", "ntl_mean_4", "ntl_mean_5", "ntl_mean_6", "ntl_mean_7", "road_length_3", "road_length_4", "road_length_5", "road_length_6", "road_length_7", "aridity_mean_3", "aridity_mean_4", "aridity_mean_5", "aridity_mean_6", "aridity_mean_7", "rugged_mean_3", "rugged_mean_4", "rugged_mean_5", "rugged_mean_6", "rugged_mean_7"]]

dhs_ntl_road_aridity_rugged.to_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\03_output\dhs_ntl_road_aridity_rugged.csv", index = True)





#adjusting everything for popluation

#population import 
dhs_pop = dhs.copy()
for i in [*range(3,8,1)]:
    dir = str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\05_population_density\pop_" + str(i) + ".csv")
    pop = pd.read_csv(dir)
    pop = pop[["DHSCLUST", "mean"]]
    pop.rename(columns = {"mean":str("pop_mean_"+str(i)), }, inplace=True)
    dhs_pop = dhs_pop.merge(pop, left_on = "cluster", right_on = "DHSCLUST")

#drop trash
dhs_pop = dhs_pop[["cluster", "quant_sep", "score_sep","pop_mean_3", "pop_mean_4", "pop_mean_5", "pop_mean_6", "pop_mean_7"]]

#create new DF
pop_devided = dhs_ntl_road.copy()

#for pop_col in ["pop_mean_3", "pop_mean_4", "pop_mean_5", "pop_mean_6", "pop_mean_7"]:
#    for var_col in ["ntl_mean_3", "ntl_mean_4", "ntl_mean_5", "ntl_mean_6", "ntl_mean_7"]
#        print(dhs_pop[i])

for i in [*range(3,8,1)]:
    pop = str("pop_mean_" +str(i))
    ntl = str("ntl_mean_" +str(i))
    road = str("road_length_" +str(i))
    pop_devided[ntl] = pop_devided[ntl]/dhs_pop[pop] 
    pop_devided[road] = pop_devided[road]/dhs_pop[pop] 

pop_devided.to_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\03_output\dhs_ntl_road_pop.csv", index = True)
























