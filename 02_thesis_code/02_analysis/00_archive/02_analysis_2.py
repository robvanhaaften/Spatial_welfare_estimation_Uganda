# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:45:42 2021

analyse the disagregated roads data 
identify the signficant variables 
analyse again with those varaibles
compare the models for different diameter size 
compare the models with dropped insiginificant variables 
output data set for further analysis 

@author: Rob
"""

import pandas as pd
import statsmodels.formula.api as sm
from statsmodels.iolib.summary2 import summary_col
from sklearn.preprocessing import StandardScaler


#import cleaned data from 
dhs_roads = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\dhs_roads_split.csv")

# standardize the indepndent variables by subtracting the mean and deviding by the standard deviation)
# xi_standard = (xi – mean(x)) / sd(x) 
dhs_roads = dhs_roads.copy()
dhs_roads.iloc[:,3:] = StandardScaler().fit_transform(dhs_roads.iloc[:,3:])


# make list of variables 
variables_list = list(dhs_roads)

# make dictionary to store signficiant variables 
variables_sig = {"3":[], "4":[], "5":[], "6":[], "7":[]}

#dictionary to store model resutls 
results = {}



for i in [*range(3,8,1)]: 
    # filter variables_list using list comprehensen to only give for length i
    variables = [d for d in variables_list if str(i) in d]
    #join the list into string sperated by a plus sign to create regression formula 
    sep = " + "
    variables = sep.join(variables)
    # make regression formula 
    formula = str("wi ~ %s" %(variables))
    # regression  
    reg1 = sm.ols(formula = formula, data = dhs_roads).fit(cov_type='cluster', cov_kwds={'groups': dhs_roads['strata']})
    
    #add adjusted r-squared to reg1 dictionary
    results[str(i)] = [round(reg1.rsquared_adj,3)]

    
    
    #make a list of variables that have p>|t| < 0.05
    #get series of p-values from regression results
    pvalues = reg1.pvalues

    #go through series of p-values and append to list if p < 0.05
    for val in pvalues:
        if val < 0.05:
            variables_sig[str(i)].append(pvalues[pvalues == val].index[0])
    
    
###do regression again but only with variables that were significant (p < 0.05) in first regression  
for d in [*range(3,8,1)]: 
    #get list of variables for the formula variables_sig dictionary 
    variables_form = variables_sig[str(d)][1:]
    #join the list into string sperated by a plus sign to create regression formula 
    sep = " + "
    variables_form = sep.join(variables_form)
    formula = str("wi ~ %s" %(variables_form))
    reg2 = sm.ols(formula = formula, data = dhs_roads).fit(cov_type='cluster', cov_kwds={'groups': dhs_roads['strata']})

    #add adjusted r-squared to results dictionary
    results[str(d)] += [round(reg2.rsquared_adj, 3)]
    #add difference in adjusted r-squareds of the two models to results dictionary
    diff = results[str(d)][1] - results[str(d)][0]
    results[str(d)] += [round(diff, 4)]
    
# make dataframe from results dictionary and fix column names 
results = pd.DataFrame.from_dict(results, orient ="index", columns =  ["full model", "reduced model", "difference"])

# save results table to csv
results.to_csv()
print(results)

#export data for model
data_out = ["cluster"]
data_out += variables_sig["3"][1:]
data_out = dhs_roads[data_out]

data_out.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\03_road\roads_split\dhs_roads_split_best.csv")


"""
conclussions: 
-difference between full and reduced model is negligable 
-3 km gridsize is has highest r-squared  
"""

# make regression summaries for tables 
# make dataframe for regressions 3km
# make list of 3km road variables 
variables_3 = variables = [i for i in variables_list if str(3) in i]
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

# drop al the non-3 km observations 
reg_out_data = reg_out_data[reg_out_data.columns[~(reg_out_data.columns.str.endswith('length'))]]

# turn list of variables into formula 
sep = " + "
variables = sep.join(list(reg_out_data)[4:])

# regression full model
formula = str("Wealth_index ~ %s" %(variables))
reg1 = sm.ols(formula = formula, data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': reg_out_data['strata']})

# regression reduced model
variables = "Path + Primary + Residential + Secondary + Tertiary + Trunk + Unclassified"
formula = str("Wealth_index ~ %s" %(variables))
reg2 = sm.ols(formula = formula, data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': reg_out_data['strata']})

# make 
regressor_order =["Intercept", "Path", "Primary", "Residential", "Secondary", "Tertiary", "Trunk", "Unclassified"]
output = summary_col([reg1,reg2],stars=True,float_format="%0.3f", model_names=["Full model","Reduced model"],info_dict={"N":lambda x: "{0:d}".format(int(x.nobs))}, regressor_order= regressor_order )
print(output)

# convert regression summaries to table and save that table to csv
reg_out_table = output.tables
reg_out_table[0].to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\tables\regression_analysis2.csv")


# save 3km model data to csv for analysis 3 
reg_out_data.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\02_analysis2\dhs_road_split_3km.csv")

























