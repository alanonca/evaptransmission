import numpy as np
import scipy.stats
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import adfuller
# import matplotlib.pyplot as plt

#input timeseries1[array], timeseries2[array], offset[days]
def comparison(data1, data2, offset):
	# +ve offest -> data2 after data1
	if len(data1) <= offset or len(data2) <= offset:
		print('Warning: timeseries.comparison data shorter or equal in length to offset') 

	if offset >= 0:
		data1_trunc = data1[offset:]
		data2_trunc = data2[:len(data2)-offset]
	else:
		data1_trunc = data1[:len(data1)+offset]
		data2_trunc = data2[-offset:]

	# compare data after offset
	corrp, pvalp = scipy.stats.pearsonr(data1_trunc, data2_trunc)
	# print('Pearsons correlation: %.3f' % corrp)
	# print('Pearsons p value: %.3f' % pvalp)

	corrs, pvals = scipy.stats.spearmanr(data1_trunc, data2_trunc)
	# print('Spearmans correlation: %.3f' % corrs)
	# print('Spearmans p value: %.3f' % pvals)

	return [corrp, pvalp, corrs, pvals]

def three(df, maxOffset, stationaryTest=True, trainTestSplit=True, splitLastxRows=3, forecastDays=1, VARorderselect='aic'):
	# get training and test dataframes
	if trainTestSplit:
		df_train, df_test = df[0:-splitLastxRows], df[-splitLastxRows:]
	else:
		df_train = df

	# stationary test
	if stationaryTest:
		for col in range(3):
			print(col)
			testdf=df_train.iloc[:,col]
			stationary(testdf)
			print('------------------------------------')

	# model fitting using all data (ad)
	model_ad = VAR(df)
	results_ad = model_ad.fit(maxlags=maxOffset, ic=VARorderselect)

	lag_order = results_ad.k_ar

	if not trainTestSplit:
		print(results_ad.summary())

		#plot forecast
		results_ad.forecast(df.values[-lag_order:], forecastDays)
		fig_forecast = results_ad.plot_forecast(forecastDays)

		return fig_forecast

	else:
		#plot current
		results_ad.forecast(df.values[-lag_order:], 0)
		fig_current = results_ad.plot_forecast(0)

		#parameters for training and test split
		forecastDays = splitLastxRows

		# model fitting
		model = VAR(df_train)
		results = model.fit(maxlags=maxOffset, ic=VARorderselect)
		print(results.summary())

		# forecast
		lag_order = results.k_ar
		results.forecast(df.values[-lag_order:], forecastDays)

		# plot forecast
		fig_split = results.plot_forecast(forecastDays)

		# evaluate forecast
		fevd = results.fevd(maxOffset)
		fevd.summary()

		return [fig_current, fig_split]
	

# Augmented Dickey-Fuller Test (ADF Test) / unit root test
def stationary(col, signif=0.05):
    dftest = adfuller(col, autolag='AIC')
    adf = pd.Series(dftest[0:4], index=['Test Statistic','p-value','# Lags','# Observations'])
    for key,value in dftest[4].items():
       adf['Critical Value (%s)'%key] = value
    print(adf)
    p = adf['p-value'] 
    #if p <= signif:
    #    print(f' Series is Stationary')
    #else:
    #    print(f' Series is Non-Stationary')
