import timeseries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# get sample dataframe df of many row and 3 columns
macrodata = sm.datasets.macrodata.load_pandas().data
df = macrodata.iloc[:, 2:5]
# print(type(df))
# print(df)

# Function comparing 3 timeseries:
# timeseries.three(df[pandas dataframe], maxOffset[int], stationaryTest[bool]=True, trainTestSplit[bool]=True, 
# 	splitLastxRows[int]=4, forecastDays[int]=10, VARorderselect='aic')

# More explanation of the parameters:
# Vector autoregression of 3 timeseries: settling time, viability and daily new cases percentage increase
# 	each being a column in df
# The model determines the dependence of new cases percentage increase on a particular day using data of all
# 	3 columns from the day before to 'maxOffset' days before as the dependent variables
# stationaryTest checks whether data in each column is staionary which is a prerequisite to do this regression
# 	analysis. If set True the result is printed in command line, if set False test is not preformed
# trainTestSplit splits all rows into a training dataset and a testing dataset if set True, and the last 
# 	'splitLastxRows' rows will be set as the testing dataset, the rest as training dataset. If set False, 
# 	all data will be used as training data
# splitLastxRows is the number of rows put into the testing dataset. This variable is only used if trainTestSplit=True
# forecastDays is the number of days to forecast into the future using all current data as training dataset, 
# 	this vairable is only used if trainTestSplit=False
# VARorderselect is the method that the model uses to determine the actual lag/offset within the maxOffset
# 	defined earlier. Possible values are {‘aic’, ‘fpe’, ‘hqic’, ‘bic’, None}. Try different ones if 
# 	the default aic is not giving expected lag

# Split original data into training and test dataset and see if model predicts known data well
[fig_current, fig_split] = timeseries.three(df, 14, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)

# Use all data as training data and forecast into the future
fig_forecast = timeseries.three(df, 14, trainTestSplit=False, forecastDays=10)

# show fig_current, fig_split and fig_forecast
plt.show() 