import linreg
import pandas as pd

# # Apr + contour
# for county in ['Harris', 'King', 'LA', 'Maricopa', 'SantaClara']:

# 	arL4csv = '20201008_' + county + '_April_output_arL5.csv'
# 	contourcsv = '20201008_contourdata_' + county + '_arL5.csv'

# 	print("\n\n")
# 	print(county)

# 	df = pd.read_csv(arL4csv, header=None)
# 	dfContour = pd.read_csv(contourcsv, header=None)

# 	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
# 		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5', 'ncperc']
# 	dfContour.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
# 		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5']

# 	linreg.trainTestSplit(df, lastxRowForTest=4, filename=arL4csv, 
# 		contourProcess = True, dfContour = dfContour)

# ------------------------------------------------------------------------------

# # May to July
# for county in ['Harris', 'King', 'LA', 'Maricopa', 'SantaClara']:

# 	arL4csv = '20201012_' + county + '_May_to_Jul_arL5.csv'

# 	print("\n\n")
# 	print(county)

# 	df = pd.read_csv(arL4csv, header=None)
# 	dfContour = pd.read_csv(contourcsv, header=None)

# 	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
# 		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5', 'ncperc']

# 	linreg.trainTestSplit(df, lastxRowForTest=21, filename=arL4csv)

# ------------------------------------------------------------------------------

# May to Aug, Maricopa only
arL4csv = '20201012_Maricopa_May_to_Aug_arL5.csv'

df = pd.read_csv(arL4csv, header=None)
df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
	'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'tsetL5', 'viabilityL5', 'ncperc']

linreg.trainTestSplit(df, lastxRowForTest=21, filename=arL4csv)