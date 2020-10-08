import pandas as pd
import nntimeseries

# for county in ['Harris', 'King', 'LA', 'Maricopa', 'MiamiD', 'SantaClara', 'SD']:
for county in ['Maricopa_May_to_Aug']:
	print(county)

	arL4csv = 'output_' + county + '_arL4.csv'
	# contourcsv = 'contourdata_' + county + '_RNNin.csv'

	df = pd.read_csv(arL4csv, header=None)
	# dfContour = pd.read_csv(contourcsv, header=None)
	
	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'ncperc']
	# dfContour.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
	# 	'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4']

	nntimeseries.main(df, offset=0, numInput=10, numHidden=70, maxEpochs=1e5, learnRate=1e-4, 
		TrainTestSplit=True, lastxRowForTest=30)
	# nntimeseries.main(df, offset=0, numInput=10, numHidden=70, maxEpochs=1e5, learnRate=1e-4, 
	# 	TrainTestSplit=True, lastxRowForTest=4, contourProcess = True, dfContour = dfContour)