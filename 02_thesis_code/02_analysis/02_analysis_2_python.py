# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:45:42 2021
@author: Rob

1. Regress the complete disagregated roads data for 3-kilometer gridsize 
2. Regress the reduced model by using only the significant variables from part 1
3. Make regression output tables 

"""

import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.iolib.summary2 import summary_col
from sklearn.preprocessing import StandardScaler


# 1. Regress the complete disagregated roads data for 3-kilometer gridsize 
# Import the clean disaggragated road data 
dhs_roads = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\dhs_roads_split.csv")

# Standardize the indepndent variables by subtracting the mean and deviding by the standard deviation)
# xi_standard = (xi – mean(x)) / sd(x) 
dhs_roads = dhs_roads.copy()
dhs_roads.iloc[:,4:] = StandardScaler().fit_transform(dhs_roads.iloc[:,4:])

# Filter variables_list for 3 kilometer grid-size 
variables_3km = [d for d in list(dhs_roads) if "3" in d]

# Join the list into string sperated by a plus sign to create regression formula 
variables_formula = " + ".join(variables_3km)
# Make regression formula 
formula = str("wi ~ %s" %(variables_formula))
# Regression 1 with all variables 
reg1 = sm.ols(formula = formula, data = dhs_roads).fit(cov_type='cluster', cov_kwds={'groups': dhs_roads['strata']})

# Get series of p-values from regression results
pvalues = reg1.pvalues

# Go through p-values and append the varaibles to variables_sig if p < 0.05
variables_sig = []
for val in pvalues:
    if val < 0.05:
        variables_sig.append(pvalues[pvalues == val].index[0])
    
# 2. Regress the reduced model by using only the significant variables from part 1
# get list of variables for the formula variables_sig dictionary 
variables_formula = variables_sig[1:]
#join the list into string sperated by a plus sign to create regression formula 
variables_formula = " + ".join(variables_formula)
formula = str("wi ~ %s" %(variables_formula))
reg2 = sm.ols(formula = formula, data = dhs_roads).fit(cov_type='cluster', cov_kwds={'groups': dhs_roads['strata']})
    

# 3. Make regression output tables 
# make data frame for final regression output and rename variable  
reg_out_data = dhs_roads.copy()
reg_out_data.rename(columns = {
    
    "wi"                                : "Wealth_index",
    "highway_bridleway3length"          : "Bridleway", 
    "highway_construction3length"       : "Construction", 
    "highway_crossing3length"           : "Crossing", 
    "highway_cycleway3length"           : "Cycleway", 
    "highway_footway3length"            : "Footway", 
    "highway_living_street3length"      : "Living_street", 
    "highway_motorway3length"           : "Motorway", 
    "highway_motorway_link3length"      : "Motorway_link", 
    "highway_path3length"               : "Path", 
    "highway_pedestrian3length"         : "Pedestrian", 
    "highway_primary3length"            : "Primary", 
    "highway_primary_link3length"       : "Primary_link", 
    "highway_proposed3length"           : "Proposed", 
    "highway_residential3length"        : "Residential", 
    "highway_road3length"               : "Road", 
    "highway_secondary3length"          : "Secondary", 
    "highway_secondary_link3length"     : "Secondary_link", 
    "highway_service3length"            : "Service", 
    "highway_steps3length"              : "Steps",
    "highway_tertiary3length"           : "Tertiary", 
    "highway_tertiary_link3length"      : "Tertiary_link", 
    "highway_trunk3length"              : "Trunk", 
    "highway_trunk_link3length"         : "Trunk_link", 
    "highway_unclassified3length"       : "Unclassified"
    
    }, inplace=True)

# Keep only road length data 
reg_out_data = reg_out_data[reg_out_data.columns[~(reg_out_data.columns.str.endswith('length'))]]

# Turn list of variables into formula 
variables_formula = " + ".join(list(reg_out_data)[4:])

# Regression full model
formula = str("Wealth_index ~ %s" %(variables_formula))
reg1 = sm.ols(formula = formula, data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': reg_out_data['strata']})

# Regression reduced model
formula = str("Wealth_index ~ Construction + Cycleway + Footway + Living_street + Path + Pedestrian + Primary + Residential + Road + Secondary + Steps + Trunk + Unclassified")
reg2 = sm.ols(formula = formula, data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': reg_out_data['strata']})

# Combine the two regression outputs into one 
regressor_order =[
    "Intercept",
    'Construction',
    'Cycleway',
    'Footway',
    'Living_street',
    'Path',
    'Pedestrian',
    'Primary',
    'Residential',
    'Road',
    'Secondary',
    'Steps',
    'Trunk',
    'Unclassified'
     ]


output = summary_col([reg1,reg2],stars=True,float_format="%0.02f", model_names=["Full model","Reduced model"],info_dict={"N":lambda x: "{0:d}".format(int(x.nobs))}, regressor_order= regressor_order )
print(output)

# Convert regression summaries to table and save that table to csv
reg_out_table = output.tables
reg_out_table[0].to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\tables\regression_analysis2.csv")


# Save 3km model data to csv for analysis 3 
reg_out_data.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\02_analysis2\dhs_road_split_3km.csv")





















