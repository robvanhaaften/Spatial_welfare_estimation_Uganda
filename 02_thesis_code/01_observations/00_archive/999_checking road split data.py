# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:21:47 2021

###OLD SCRIPT###

##first part, cleaning and merging, is moved to qgis file 03_road_split
##second part, analysis, is moved to analysis_2 document 
merging roads and preliminary analysis 
@author: Rob
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
import numpy as np 

from pathlib import Path
from pathlib import PureWindowsPath

#make list of file paths of aggregated roads files 
road_csvs_obj = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\\').rglob("*merged.csv")
road_csvs = [str(x) for x in road_csvs_obj]
print(road_csvs)

#import dhs
dhs = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\04_DHS\ug_dhs_wi.csv")

dhs_roads = dhs.copy() 

#cleaning merged files python files 

#for making variables list of lists 
variables = []

for i in road_csvs:
    road = pd.read_csv(i)
    #make wide by grouping by cluster
    road = road.groupby(by = "DHSCLUST").max()
    #road.drop(["highway_Un maintained track3length"],  1)
    #drop everything but length
    road = road[road.columns[(road.columns.str.endswith('length'))]]
    road = road[road.columns[(~road.columns.str.contains("maintained"))]]
    variables.append(list(road))
    dhs_roads = dhs_roads.merge(road, left_on = "cluster", right_index = True)



for i in variables: 
    sep = " + "
    variables = sep.join(i)
    formula = str("score_sep ~ %s" %(variables))
    results = sm.ols(formula = formula, data = dhs_roads).fit().rsquared
    print(results)
