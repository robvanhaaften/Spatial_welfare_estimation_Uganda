# -*- coding: utf-8 -*-
"""
Created on Thu May 27 12:03:38 2021

@author: Rob

merge and clean DHS and GIS output for ntl visible, stable and road lengths 
"""
import numpy as np
import pandas as pd 
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

###import/clean/transform### 
#import csvs
dhs = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\01_input\04_DHS\WI_uganda_rural.csv")
gis = pd.read_csv(r"C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\grid_observations\NTL_road_merged.csv")

#sort out gis merge formating mess 
gis = gis.groupby(by = "DHSCLUST").mean()

#merge
dhs_gis = pd.merge(dhs, gis,  left_on="hv001", right_on="DHSCLUST")

#rename dhs variables 
dhs_gis.rename(columns = {"hv001":"cluster", "hv025":"urban_rural", "hv270":"quant_com", "hv271":"score_com", "hv270a":"quant_sep", "hv271a":"score_sep"}, inplace=True)
#keep relevant data 
dhs_gis = dhs_gis[['cluster','score_sep', 'vis3mean', 'vis4mean', 'vis5mean', 'vis6mean', 'vis7mean', 'road3length', 'road4length', 'road5length', 'road6length', 'road7length']]

#make logs for all observations and add to dataframe
for elem in dhs_gis.columns[2::]:
    dhs_gis[str(elem + "log")] = np.log10(dhs_gis[elem])

###analysis### 
#make df
results = pd.DataFrame({"variable":[], "r-squared":[], "intercept":[], "slope":[]}, columns = ['variable', 'r-squared', 'intercept', "slope"])

#change inf values to nan
for elem in dhs_gis.columns[2::]:
    dhs_gis.replace([np.inf, -np.inf], np.nan, inplace=True)


#calculate regression results and append to results df
for elem in dhs_gis.columns[2::]:
    rsq = sm.ols(formula=str("score_sep ~ %s" %(elem)), data=dhs_gis).fit().rsquared
    params = sm.ols(formula=str("score_sep ~ %s" %(elem)), data=dhs_gis).fit().params
    print(str(elem) + "\n" +str(rsq))
    new_row = {'variable':elem, 'r-squared':rsq, 'intercept':params[0], 'slope':params[1]}
    results = results.append(new_row, ignore_index=True)
    
    
#make scatter plots 
for elem in dhs_gis.columns[2::]:
    plt.scatter(dhs_gis["score_sep"], dhs_gis[elem])
    plt.title(elem)
    plt.figure()



    
    
    