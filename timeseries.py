import numpy as np
import scipy.stats

#input timeseries1[array], timeseries2[array], offset[days]
def comparison(data1, data2, offset):
	# +ve offest -> data2 after data1
	if len(data1) <= offset or len(data2) <= offset:
		print('Warning: timeseries.comparison data shorter or equal in length to offset') 

	if offset >= 0:
		data1_trunc = data1[offset:]
		data2_trunc = data2[:len(data2)-offset]
	else:
		data1_trunc = data1[:len(data1)+offset]
		data2_trunc = data2[-offset:]

	# print(data1)
	# print(data2)	
	# print(data1_trunc)
	# print(data2_trunc)

	# compare data after offset

	corrp, pvalp = scipy.stats.pearsonr(data1_trunc, data2_trunc)
	# print('Pearsons correlation: %.3f' % corrp)
	# print('Pearsons p value: %.3f' % pvalp)

	corrs, pvals = scipy.stats.spearmanr(data1_trunc, data2_trunc)
	# print('Spearmans correlation: %.3f' % corrs)
	# print('Spearmans p value: %.3f' % pvals)

	return [corrp, pvalp, corrs, pvals]