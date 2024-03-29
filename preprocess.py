import pandas as pd
import sklearn
from matplotlib import pyplot




## TO DO:
# 1. create command line for train models and experimenting with different algorithms
# 2. create a UI that visualize the model metrics for each model after training


## How package is expected to be used
#1. developer preovides path of data and the target variable in the data.
#2 has option to also specify column names of predictors to use. if not provided, all columns will be used
#3. option to specify data type of the columns
# option to define tabs to show on ui after training, mapping to change the names of the tabs with dict 
#4. data format is csv for now,
# option to define whether to export code
#5. the parameters to pass can defined in a config file of format json



## UI 
#1. features of the UI
#2. page for visualizing graphs of models metric by comparing diff models
#3. page for using model for prediction - contains inputs for selecting values for predictors used for modeling


##  API 
#1. The model should be packaged as a REST API
#2. check to find free port for running the model api

## OUTPUT OF running the package
#1. Artefact
#a. code of app ui for deployment
#b. code for model api for deployment



## what the package does
# the package preprocesses the data, undertakes feature engineering, defines anumber of models based on target var,
# and train each of those models, evaluate model using cross validation of 20 steps using metric define and stores the
# results. 
#. The exported results is then read and visualized on a dash app
# The predictors are used to define type of inputs and their unique values used to define values to select from 
# on the prediction page.
# The best model based on metrics is selected, exported and used to build an API which is run
# Each time a user selects inputs and click the predict button on the prediction page, the values are sent to the api,
# prediction is made and results are sent back. The results are preprocess and displayed on the prediction page













