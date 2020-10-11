import pandas as pd
import nntimeseries

# Apr + contour
for county in ['Harris', 'King', 'LA', 'Maricopa', 'SantaClara']:
	print(county)

	arL4csv = '20201008_' + county + '_April_output_arL5.csv'
	contourcsv = '20201008_contourdata_' + county + '_arL5.csv'

	df = pd.read_csv(arL4csv, header=None)
	dfContour = pd.read_csv(contourcsv, header=None)
	
	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5', 'ncperc']
	dfContour.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5']

	# nntimeseries.main(df, offset=0, numInput=10, numHidden=70, maxEpochs=1e5, learnRate=1e-4, 
	# 	TrainTestSplit=True, lastxRowForTest=30)
	nntimeseries.main(df, offset=0, numInput=12, numHidden=70, maxEpochs=1e5, learnRate=1e-4, 
		TrainTestSplit=True, lastxRowForTest=4, contourProcess = True, dfContour = dfContour)