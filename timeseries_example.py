import timeseries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# get sample dataframe df of many row and 3 columns
macrodata = sm.datasets.macrodata.load_pandas().data
df = macrodata.iloc[:, 2:5]
print(type(df))
print(df)

# timeseries.three(df[pandas dataframe], maxOffset[int], stationaryTest[bool]=True, trainTestSplit[bool]=True, 
# 	splitLastxRows[int]=4, forecastDays[int]=10)
# Vector autoregression of 3 timeseries: settling time, viability and daily new cases percentage increase

[fig_current, fig_split] = timeseries.three(df, 14, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
fig_forecast = timeseries.three(df, 14, trainTestSplit=False, forecastDays=10)

plt.show() # show fig_current, fig_split and fig_forecast