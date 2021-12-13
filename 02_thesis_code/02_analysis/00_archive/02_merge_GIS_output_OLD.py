# -*- coding: utf-8 -*-
"""
Created on Mon May 24

@author: Rob

Purpose:
Merge csv outputs from gis data with dhs data
make a clean dataframe 
add quadratic and log transformations 

"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm

#dhs, rename and drop
dhs = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\01_input\04_DHS\ug_dhs_wi.csv")
dhs = dhs[["cluster","score_sep"]]

#NTL
ntl_vars = ["stab3", "stab4","stab5","stab6","stab7", "vis3","vis4","vis5","vis6","vis7"]

ntl_dat = dhs
for i in ntl_vars:
    ntl_temp = pd.read_csv(str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\grid_observations\%s.csv" %i))
    #print(ntl_temp[str((i) + "mean")])



#NTL merge and analysis 
for i in ntl_vars:
    var = i + "mean"
    ntl_in = pd.read_csv(str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\01_NTL\grid_observations\%s.csv" %i))
    ntl = ntl_in[["DHSCLUST", str(i + "mean")]]
    ntl = pd.merge(dhs, ntl, left_on="cluster", right_on="DHSCLUST")
    #calculate stats
    form = str("score_sep ~ %s" %(var))
    results = sm.ols(formula=form, data=ntl).fit().params
    result = sm.ols(formula=form, data=ntl).fit().rsquared
    print(str(i) + "   " +  str(result))

    #make scatter
    plt.scatter(ntl["score_sep"], ntl[var])
    plt.title(str(i) + "  r-squared = " + str(result))
    plt.figure()


    #add line
    #x = np.linspace(-150000,400000)
    #y = results[0] + results[1]*x
    #print(results)
    #plt.plot(x,y)



##sample difference is the non-georeferenced data

#road
road_vars = ["road3", "road4", "road5", "road6", "road7"]
for i in road_vars:
    road = pd.read_csv(str(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\road_aggregate\%s.csv" %i))
    road = pd.merge(dhs, road, left_on="cluster", right_on="DHSCLUST")
    ###its actually length3
    results = sm.ols(formula=str("score_sep ~ %slength" %(i)), data=road).fit().params
    result = sm.ols(formula=str("score_sep ~ %slength" %(i)), data=road).fit().rsquared
    print(str(i) + "   " +  str(result))
    plt.scatter(road["score_sep"], road[str("%slength" %(i))])
    plt.title(str(i) + "  r-squared = " + str(result))
    plt.figure()


    ##add line
    #x = np.linspace(-150000,400000)
    #y = results[0] + results[1]*x
    #print(results)
    #plt.plot(x,y)






