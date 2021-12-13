# -*- coding: utf-8 -*-

"""
Created on Mon Apr 19 17:20:51 2021
@author: Rob

Cleans dhs data 
Groups by cluster taking the mean value for households in the observation
Keeps only the combined wealth index, cluster and strata variables 

"""

import pandas as pd

# import dhs survey data
# source: https://www.dhsprogram.com/data/dataset/Uganda_Standard-DHS_2016.cfm?flag=0
df = pd.read_stata(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\01_input\04_DHS\Uganda_2016_HH_recode\UGHR7BFL.DTA", convert_categoricals=False)

# keep the household id, cluster id, combined wealth index and sampling strata 
ug_dhs_wi = df[["hhid","hv001", "hv271", "hv023"]]
ug_dhs_wi.rename(columns = {"hv001":"cluster", "hv271":"wi", "hv023":"strata"}, inplace=True)

#group by cluster by taking mean of households in each cluster 
ug_dhs_wi = ug_dhs_wi.groupby(by = "cluster").mean()

ug_dhs_wi.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\05_dhs\ug_dhs_wi.csv", index = True)
