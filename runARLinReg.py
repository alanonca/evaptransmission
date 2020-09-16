import linreg
import pandas as pd

# for csvName in ['output_Clark_arL4.csv', 'output_Harris_arL4.csv', 'output_King_arL4.csv', 
# 	'output_LA_arL4.csv', 'output_Maricopa_arL4.csv', 'output_MiamiD_arL4.csv', 
# 	'output_SantaClara_arL4.csv', 'output_SD_arL4.csv']:

for csvName in ['output_LA_new_arL4.csv']:

	print("\n\n")
	print(csvName)
	df = pd.read_csv(csvName, header=None)
	df.columns = ['tsetL0', 'viabilityL0', 'tsetL1', 'viabilityL1', 'tsetL2', 'viabilityL2', 
		'tsetL3', 'viabilityL3', 'tsetL4', 'viabilityL4', 'ncperc']
	linreg.trainTestSplit(df, lastxRowForTest=4, filename=csvName)
	# linreg.regOnly(df)