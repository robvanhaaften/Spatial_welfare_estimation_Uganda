# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:21:38 2021

@author: Rob


Roads PCA merge 
"""
from pathlib import Path
from pathlib import PureWindowsPath
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import scale 
from sklearn import model_selection
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#makes list of directories of all merged GIS files 
road_csvs_obj = Path(r'C:\Users\Rob\Dropbox\My PC (DESKTOP-DP7OCOF)\Desktop\GIS_thesis\01_thesis_data\02_temp\02_road\roads_split\zonal_stats\\').rglob("*merged.csv")
road_csvs = [str(x) for x in road_csvs_obj]

#create dictionary to store the dataframes in 
grid_dfs = {}

#loop over files, add them to dictionary and group each by cluster to clean GIS mess 
for csv in road_csvs:
    df_name = str(PureWindowsPath(csv).name )
    grid_dfs[df_name] =  pd.read_csv(csv)
    grid_dfs[df_name] = grid_dfs[df_name].groupby(by = "DHSCLUST").mean()
    grid_dfs[df_name]


#removing duplicates


# duplicates = pd.Series(grid_dfs["grid_extract_3_merged.csv"].duplicated(subset = ["id"], keep = False))
# grid3 = grid_dfs["grid_extract_3_merged.csv"]
# grid3["duplicates"] = pd.Series(grid3.duplicated(subset = ["id"], keep = False))
# grid3 = grid3[]
# ug_dhs_r = ug_dhs[(ug_dhs.hv025 == 2)]


#MOVE THIS SHIT TO NEXT FILE 
###PCA
#scale data

df = grid_dfs["grid_extract_3_merged.csv"]
dhs = pd.read_csv(r"C:\Users\Rob\Desktop\GIS_thesis\01_thesis_data\01_input\04_DHS\WI_uganda_rural.csv", index_col=0)
xy = pd.merge(df, dhs, left_index=True, right_index=True)
x = xy.filter(regex = "length$", axis = "columns")
y = xy.filter(regex = "hv271a$", axis = "columns")

pca = PCA()
x_reduced = pca.fit_transform(scale(x))

#cross validation
cv = RepeatedKFold(n_splits=10, n_repeats=2, random_state=1)

regr = LinearRegression()
mse = []
score = -1*model_selection.cross_val_score(regr,
            np.ones((len(x_reduced),1)), y, cv=cv,
            scoring='neg_mean_squared_error').mean()    
mse.append(score)


# Calculate MSE using cross-validation, adding one component at a time
for i in np.arange(1, 6):
    score = -1*model_selection.cross_val_score(regr,
                x_reduced[:,:i], y, cv=cv, scoring='neg_mean_squared_error').mean()
    mse.append(score)
    
# Plot cross-validation results    
# plt.plot(mse)
# plt.xlabel('Number of Principal Components')
# plt.ylabel('MSE')
# plt.title('hp')
# plt.figure()
# #VARIATION PER COMPONENT
# print(np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100))

# comps = pca.components_


# for i in grid_dfs:
pc = PCA(n_components=2)
pc = pc.fit_transform(df[df])
print(df)
print("components:", pca.components_)
comp = pca.components_
print("mean:      ", pca.mean_)
print("covariance:", pca.get_covariance()) 

