This folder contains all the scripts used for my MSc thesis

Titel: Spatial welfare estimation in Uganda: Combining nighttime lights, road networks, and aridity for welfare mapping in Uganda 

Abstract:
Insufficient data on economic welfare in the developing world hinders research and decision-making. In low-income countries, data availability on welfare is particularly lacking. The conventional approach for gathering data on welfare in developing countries is to conduct household surveys. However, this method is too resource-intensive to meet the growing demand for data. An alternative is to use spatial proxies for welfare estimation. The most popular proxies to date are Nighttime Light (NTL) satellite data and daytime satellite imagery. While these methods are promising, the accuracy is comparatively lower for low-income countries and agricultural economies. This study aims to improve spatial welfare in these contexts by combining data on NTL, road networks, and aridity. To develop the model, we want to know at what scale to conduct the analysis and whether adding data on road infrastructure and aridity improves the conventional proxy of using only NTL. The model is estimated using the asset-based wealth data from the 2016 Ugandan Demographic and Health Surveys (DHS) Standard survey and validated using the same index from the 2018-19 Ugandan DHS Malaria Indicator Survey. We first find that estimation works best at a 3-kilometer grid size. However, further study is recommended on finding the appropriate scale for similar analyses. Furthermore, it is found that the road network disaggregated by its respective road types is a good proxy, explaining 66% of the variation in welfare. Moreover, the model combining NTL, a selection of road types, and the aridity index adjusted for the occurrence of irrigation is also an improvement compared to using only NTL. Using only NTL as an estimator explains 39% of the variation in asset-based wealth while the combined model explains 70% of the variation. Finally, the model explains 66% of the variation of welfare when validated with the 2018-19 DHS survey data. Based on these findings, we recommend further investigation into the variables used in this study, and other variables relevant to rural development, in combination with more advanced estimation methods. 


The scripts are organized in 4 folders. 
In the following a short description is given for each folder and the script. For more details see the comments in the scripts. All scripts with the suffix "_QGIS" have to be run in the QGIS python console. Scripts with the suffix "_python" can be run in a normal Python console. 

###01_observations###
This folder contains the scripts used to calculate, clean and merge the observations. 

01_create_gridcells_QGIS
Makes the hexagonal grids which are used to extract the observations

02_ntl_QGIS
Generates the ntl observations using the Google Earth Engine 

03_road_aggragated_QGIS
Calculates the sum of all the road lengths within each hexagon with DHS observations 

04_aridity_QGIS
Calculates the average adjusted aridity index for each hexagon 

05_dhs_clean_python
Cleans dhs data 

06_merge_analysis1_python
Merges DHS, NTL, roads and adjusted arditiy index observations 

07_road_disaggragated_QGIS
Disaggragates the road network data by road type, calculates the road length for each individual road type and merges the observations into a single dataframe 

08_descriptive_statistics
Generate the following descriptive statistics: descriptive statistics table 1 for 3 KM data, kernel density plots and descriptive statistics apendix for individual road types


###02_analysis###
This folder contains all the analyses for the model estimation.

01_analysis_1_python
Univariate regressions for all input varaibles at 5 grid sizes to select best gridsize, make the scatter plots and regression table for the 3-kilometer grid size.

02_analysis_2_python
Multivariate regressions of the disaggragated road type data to select significant road types variables.

03_analysis_3_python
Make 3 regressions on wealth index: ntl, combined model with total road length and combined model with significant road types. Export coeficients to csv for making final poverty map.


###03_validation###
This folder contains the scripts to generate the observations and conduct the analysis for model validation

01_create_gridcells_mis_QGIS
Extracts the grid cells that contain observations from the DHS MIS survey

02_ntl_mis_QGIS
Generates the DHS MIS ntl observations using the Google Earth Engine (GEE) 

03_aridity_mis_QGIS
Calculates the DHS MIS average adjusted aridity index observations 

04_road_disaggragated_mis_QGIS
Calculates the road length for the disaggragated road data at 3-kilometer grid size for all the DHS MIS observations 

05_dhs_clean_mis_python
Cleans DHS MIS data by grouping by cluster (taking the mean value) and keeping the combined wealth index, cluster and strata variables 

06_estimation_validation_python
Conducts the final validation by predicting the DHS MIS observations using model coeficients from analysis 3

###04_poverty_map###
This folder contains the scripts to make the final welfare map

01_observation_uganda_grid_3_QGIS
Generates the observations for all the proxies in QGIS 

02_merge_data_export_python
Merges the output from QGIS into a single CSV to use for the final map

