Introduction 
This folder contains all the scripts used for my MSc thesis: Welfare mapping in Uganda 


-folders 
-files and suffixes 
-annotation explained 
-data sourcing 
	ntl:		Google Earth Engine API
	road network: 	humantiarian data exchange (URL: ...)
	aridity index:	Calculated from CGIAR and sentinel 2 data (URL1: ..., URL2:...)

The scripts are organized in 4 folders. 
In the following a short description is given for each folder and the scripts. For more details see the comments in the scripts. All scripts with the suffix "_QGIS" have to be run in the QGIS python console. Scripts with the suffix "_python" can be run in a normal python console. 


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





















