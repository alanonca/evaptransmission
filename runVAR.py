import timeseries
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df_csv = pd.read_csv('output_King_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_LA_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 3, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_Maricopa_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_Harris_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_MiamiD_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 1, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_Clark_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_SD_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

df_csv = pd.read_csv('output_SantaClara_four.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
[fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()