 # -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:14:39 2021
@author: Rob

1. Merge output from analysis 1 and 2 

2. Make 3 regressions on wealth index: ntl, combined model with total road length and combined model with significant road types 

3. Combine output into single table and export to csv

4. Export coeficients to csv for making final poverty map

"""

import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.iolib.summary2 import summary_col

# 1. Merge output from analysis 1 and 2 
data_analysis1 = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\01_analysis1\dhs_ntl_road_aridity_3km.csv")

data_analysis2 = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\02_analysis2\dhs_road_split_3km.csv")

data = data_analysis1.merge(data_analysis2, left_on="cluster", right_on="cluster")
data.rename(columns ={"Wealth_index_x": "Wealth_index"}, inplace=True)

# 2. Make 3 regressions on wealth index: ntl, combined model with total road length and combined model with significant road types 
# Model 1: ntl
formula =  "Wealth_index ~ Nighttime_light"
reg1 = sm.ols(formula = formula, data = data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']})

# Model 2: combined model with total road length 
formula =  "Wealth_index ~ Nighttime_light + Road_length + Adjusted_aridity_index"
reg2 = sm.ols(formula = formula, data = data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']})

# Model 3: combined model with road length by type 
formula =  "Wealth_index ~ Nighttime_light + Adjusted_aridity_index + Construction + Cycleway + Footway + Living_street + Path + Pedestrian + Primary + Residential + Road + Secondary + Steps + Trunk + Unclassified"
reg3 = sm.ols(formula = formula, data = data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']})

# print regression results  
print(reg1.summary(), reg2.summary(), reg3.summary())

# 3. Combine output into single table and export to csv
# make combined output summary of the three regressions 
regressor_order = [
                    "Intercept", 
                    "Nighttime_light", 
                    "Road_length", 
                    "Adjusted_aridity_index",
                    "Construction",
                    "Cycleway",
                    "Footway",
                    "Living_street",
                    "Path",
                    "Pedestrian",
                    "Primary",
                    "Residential",
                    "Road",
                    "Secondary",
                    "Steps",
                    "Trunk",
                    "Unclassified"
                    ]
output = summary_col([reg1, reg2,reg3],stars=True,float_format='%0.0f', model_names=["nighttime light", 'combined model 1','combined model 2'],info_dict={'N':lambda x: "{0:d}".format(int(x.nobs))}, regressor_order= regressor_order )
print(output)

# convert regression summaries to table and save to csv
reg_out_table = output.tables
reg_out_table[0].to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\tables\regression_analysis3.csv")

# 4. Export coeficients to csv for making final poverty map
# export coeficients of final model to make map in QGIS
coeficients = pd.DataFrame(reg3.params)
coeficients.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\03_analysis3\model_coeficients.csv")


