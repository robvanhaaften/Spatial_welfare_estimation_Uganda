# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:43:26 2021
@author: Rob

1. Univariate regressions for all input varaibles at 5 grid sizes 

2. Make the scatter plots for the 3-kilometer grid size 

3. Make the regression table for the 3-kilometer grid size 

"""
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from statsmodels.iolib.summary2 import summary_col
import seaborn as sns

# Set theme for plots  
sns.set_theme()
sns.set_style("whitegrid")

# Import the merged results for analysis 1
data = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\03_output\01_analysis1\data_analysis1_standardized.csv", index_col = "cluster")

# 1. Univariate regressions for all input variables 
# Make a list of independent variables names to make regression formulas 
variables= list(data)[3:]

# Dictionary to store results 
results = {}

# Loop over variable list, regress on the wealth index, make plots, and store the r-squared of each model
for var in variables:    
    # Make regresion formula and run regression with standard errors clustered on strata
    formula = str("wi ~ %s" %(var))
    reg = sm.ols(formula = formula, data = data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']}) 
    
    # Print the varaibles name and r-squared 
    print(str(var) + "\t\t"+ str(reg.rsquared))

    # Save the results to a dictionary with var name, scale and r-squared 
    results[var] = [var.split(sep = "_")[0]]
    results[var] += [var.split(sep = "_")[2]]
    results[var] += [round(reg.rsquared, 2)]
        
    
# Make a dataframe from results dictionary 
results = pd.DataFrame.from_dict(results, orient ="index", columns =  ["Variable", "Grid size", "R-squared"])

# Export results dictionary to csv file 
results.to_csv(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\Tables\grid_size_analysis.csv') 


# 2. Make the scatter plots for the 3-kilometer grid size 

# Make dataframe with wealth index and 3 km observations 
data_3km = data[["wi", "ntl_mean_3", "road_length_3", "aridity_mean_3"]]

# Make plots for results section for NTL, roads agg and aridity adj. 
# NTL
plt.figure(figsize=(8, 6))
sns.regplot(x='ntl_mean_3', y='wi', data=data, ci = 95)
plt.xlabel("Nighttime light")
plt.ylabel("Wealth index")
plt.savefig(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\plots\Figure5.pdf")
plt.figure()

# Road 
plt.figure(figsize=(8, 6))
sns.regplot(x='road_length_3', y='wi', data=data)
plt.xlabel("Total road length")
plt.ylabel("Wealth index")
plt.savefig(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\plots\Figure6.pdf")
plt.figure()

# Aridity 
plt.figure(figsize=(8, 6))
sns.regplot(x='aridity_mean_3', y='wi', data=data)
plt.xlabel("Adjusted ardity index")
plt.ylabel("Wealth index")
plt.savefig(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\plots\Figure7.pdf")
plt.figure()


# 3. Make the regression table for the 3-kilometer grid size 

# Clean variable names for regression output  
reg_out_data = data_3km.copy()
reg_out_data.rename(columns = {
    
    "wi"                : "Wealth_index", 
    "ntl_mean_3"        : "Nighttime_light", 
    "road_length_3"     : "Road_length", 
    "aridity_mean_3"    : "Adjusted_aridity_index"
    
    }, inplace=True)

# Do regressions with fixed variable names and standard errors clustered on strata
reg_ntl = sm.ols(formula = "Wealth_index ~ Nighttime_light", data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']})

reg_road = sm.ols(formula = "Wealth_index ~ Road_length", data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']})

reg_aridity = sm.ols(formula = "Wealth_index ~ Adjusted_aridity_index", data = reg_out_data).fit(cov_type='cluster', cov_kwds={'groups': data['strata']})

# Make output summary for the three univariate regressions and the combined model 
reg_out = summary_col([reg_ntl, reg_road, reg_aridity],stars=True,float_format='%0.3f', model_names=["Nighttime light", "Road length", "Adjusted aridity index"],info_dict={"N":lambda x: "{0:d}".format(int(x.nobs))},regressor_order= ["Intercept", "Nighttime_light", "Road_length", "Adjusted_aridity_index"])

# Convert regression summaries to table and save that table to csv
reg_out_table = reg_out.tables 
reg_out_table[0].to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\tables\regression_analysis1.csv")

# Save model data (to use for analysis 3)
reg_out_data.to_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\03_output\01_analysis1\dhs_ntl_road_aridity_3km.csv")

# correlation matrix ??????????????????
corr = reg_out_data[["Nighttime_light", "Road_length", "Adjusted_aridity_index"]].corr().round(2)


















