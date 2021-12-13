# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 11:06:05 2021

merge by using functions 

@author: Rob
"""




for i in [*range(3,8,1)]:
    dir = str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\road_aggregate\road"+ str(i) +".csv")
    road = pd.read_csv(dir)
    road = road[["DHSCLUST",str("road"+ str(i) + "length")]]
    road.rename(columns = {str("road"+ str(i) + "length"):str("road_length_"+str(i))}, inplace=True)
    dhs_ntl_road = dhs_ntl_road.merge(road, left_on = "cluster", right_on = "DHSCLUST")
    
    
def merge_data_dhs(path, var_in, var_out):
    dhs = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\04_DHS\ug_dhs_wi.csv")
#    for i in [*range(3,8,1)]:
    path = str(r) + path  + "3" + ".csv"
    print(path, var_in, var_out)

merge_data_dhs("C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\road_aggregate\road", road3length, road_length_)

