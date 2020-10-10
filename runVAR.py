import timeseries
import pandas as pd
# import statsmodels.api as sm
# import matplotlib.pyplot as plt

# Apr only, countour data process manually
for county in ['Harris', 'King', 'LA', 'Maricopa', 'SantaClara']:
	print(county)
	csvName = '20201008_'+county+'_April_output.csv'
	print(csvName)

	df_csv = pd.read_csv(csvName, header=None)
	df = df_csv.T # transpose
	df.columns = ['tset', 'viability', 'ncperc']
	[fig_current, fig_split] = timeseries.three(df, 5, fileName=csvName, stationaryTest=True, 
		trainTestSplit=True, splitLastxRows=4)