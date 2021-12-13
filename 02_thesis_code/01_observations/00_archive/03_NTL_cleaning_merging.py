# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 17:28:57 2021

@author: Rob
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

#import and clean NTL
stab = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\observations_csv\stab_5to10.csv")
vis = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\observations_csv\vis_5to10.csv")

filt = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\observations_csv\filt_5to10.csv")

#clean shit
stab = stab.loc[:, "DHSCLUST":]
stab.drop(stab.loc[:, "CCFIPS":"DATUM"], inplace = True, axis = 1)

vis = vis.loc[:, "DHSCLUST":]
vis.drop(vis.loc[:, "CCFIPS":"DATUM"], inplace = True, axis = 1)

filt = filt.loc[:, "DHSCLUST":]
filt.drop(filt.loc[:, "CCFIPS":"DATUM"], inplace = True, axis = 1)

#group them so they aline 
stab = stab.groupby(by = "DHSCLUST").mean()
vis = vis.groupby(by = "DHSCLUST").mean()
filt = filt.groupby(by = "DHSCLUST").mean()
filt = np.log(filt)

#merge stab and vis
ntl_data = pd.merge(stab, vis, left_index=True, right_index=True)


#Import dhs and merge with rest 
dhs = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\01_input\04_DHS\WI_uganda_rural.csv")
ntl_data = pd.merge(dhs, ntl_data,  left_on="hv001", right_index=True)

ntl_filt = pd.merge(dhs, filt,  left_on="hv001", right_index=True)

#regress visible and stable on DHS welfare
print("\nvisible r-squareds: ")
for i in range(5,11):
    form = str("hv271a ~ _vis%dmean" %(i))
    result = sm.ols(formula=form, data=ntl_data).fit().rsquared
    print(result)
    visnum = str("_vis%dmean" %(i))
    ntl_data.plot.scatter("hv271a", visnum)
    
ntl_data.plot.scatter("hv271a", "_vis5mean")
print("\nstable r-squareds: ")
for i in range(5,11):
    form = str("hv271a ~ _stab%dmean" %(i))
    result = sm.ols(formula=form, data=ntl_data).fit().rsquared
    print(result)
    stabnum = str("_stab%dmean" %(i))
    ntl_data.plot.scatter("hv271a", stabnum)
    
    
#log transform vis and stab and make a log dataframe 
stab_log = np.log(stab.replace(0, 0.0001))
vis_log = np.log(vis)
ntl_data_log = pd.merge(stab_log, vis_log,  left_index=True, right_index=True)
ntl_data_log = pd.merge(stab_log, vis_log,  left_index=True, right_index=True)
ntl_data_log = pd.merge(dhs, ntl_data_log,  left_on="hv001", right_index=True)

print("\nvisible log r-squareds: ")
for i in range(5,11):
    form = str("hv271a ~ _vis%dmean" %(i))
    result = sm.ols(formula=form, data=ntl_data_log).fit().rsquared
    print(result)
    visnum = str("_vis%dmean" %(i))
    ntl_data_log.plot.scatter("hv271a", visnum)
    

print("\nstable log r-squareds: ")
for i in range(5,11):
    form = str("hv271a ~ _stab%dmean" %(i))
    result = sm.ols(formula=form, data=ntl_data_log).fit().rsquared
    print(result)
    stabnum = str("_stab%dmean" %(i))
    #ntl_data_log.plot.scatter("hv271a", stabnum)



###for filtered visible NTL data
print("\nfiltered r-squareds: ")
for i in range(5,11):
    form = str("hv271a ~ _filt%dmean" %(i))
    result = sm.ols(formula=form, data=ntl_filt).fit().rsquared
    print(result)
    visnum = str("_filt%dmean" %(i))
    #ntl_filt.plot.scatter("hv271a", visnum)

