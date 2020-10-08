import timeseries
import pandas as pd
# import statsmodels.api as sm
# import matplotlib.pyplot as plt

# Without interaction term
print("King")
df_csv = pd.read_csv('output_King.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

print("LA")
df_csv = pd.read_csv('output_LA_new.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

print("Maricopa")
df_csv = pd.read_csv('output_Maricopa.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

print("Harris")
df_csv = pd.read_csv('output_Harris.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

print("MiamiD")
df_csv = pd.read_csv('output_MiamiD.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 2, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

print("Clark")
df_csv = pd.read_csv('output_Clark.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

# print("SD")
# df_csv = pd.read_csv('output_SD.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc']
# [fig_current, fig_split] = timeseries.three(df, 5, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

print("SantaClara")
df_csv = pd.read_csv('output_SantaClara.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']
[fig_current, fig_split] = timeseries.three(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# plt.show()

# # With interaction term
# print("King")
# df_csv = pd.read_csv('output_King_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("LA")
# df_csv = pd.read_csv('output_LA_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 3, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("Maricopa")
# df_csv = pd.read_csv('output_Maricopa_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 3, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("Harris")
# df_csv = pd.read_csv('output_Harris_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("MiamiD")
# df_csv = pd.read_csv('output_MiamiD_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 1, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("Clark")
# df_csv = pd.read_csv('output_Clark_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("SD")
# df_csv = pd.read_csv('output_SD_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()

# print("SantaClara")
# df_csv = pd.read_csv('output_SantaClara_four.csv', header=None)
# df = df_csv.T # transpose
# df.columns = ['tset', 'viability', 'ncperc', 'tsetViabilityInteract']
# [fig_current, fig_split] = timeseries.four(df, 4, stationaryTest=True, trainTestSplit=True, splitLastxRows=4)
# # plt.show()