import pandas as pd
import lstm

# Apr + contour
for county in ['Harris', 'King', 'LA', 'Maricopa', 'SantaClara']:
# for county in ['Harris']:
	print(county)

	arL4csv = '20201008_' + county + '_April_output_arL5.csv'
	contourcsv = '20201008_contourdata_' + county + '_arL5.csv'

	df = pd.read_csv(arL4csv, header=None)
	dfContour = pd.read_csv(contourcsv, header=None)
	
	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5', 'ncperc']
	dfContour.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5']

	lstm.testTrainSplit(df, numOutput=1, numLSTMunits = 120, maxEpochs=1000000, batchSize = 72, 
		lastxRowForTest=4, countyName = county, contourProcess = True, dfContour = dfContour)