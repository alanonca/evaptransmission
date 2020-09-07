import pandas as pd
import nntimeseries

df_csv = pd.read_csv('output_King.csv', header=None)
df = df_csv.T # transpose
df.columns = ['tset', 'viability', 'ncperc']

nntimeseries.main(df, offset=2, numInput=2, numHidden=10, maxEpochs=1e3, learnRate=1e-6)