import pandas as pd
import nntimeseries

for csvName in ['output_Clark_arL4.csv', 'output_Harris_arL4.csv', 'output_King_arL4.csv', 
	'output_LA_arL4.csv', 'output_Maricopa_arL4.csv', 'output_MiamiD_arL4.csv', 
	'output_SantaClara_arL4.csv', 'output_SD_arL4.csv']:

	df = pd.read_csv(csvName, header=None)
	print(csvName)

	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'ncperc']

	nntimeseries.main(df, offset=0, numInput=10, numHidden=70, maxEpochs=1e5, learnRate=1e-4, 
		TrainTestSplit=True, lastxRowForTest=4)