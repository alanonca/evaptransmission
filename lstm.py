from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy

def testTrainSplit(df, numOutput, numLSTMunits, maxEpochs, batchSize, lastxRowForTest, countyName, 
	contourProcess = False, dfContour = None):

	dftrain = df.head(df.shape[0]-lastxRowForTest)
	dftest = df.tail(lastxRowForTest)
	 
	train_X, train_y = dftrain.iloc[:, :-1], dftrain.iloc[:, -1]
	test_X, test_y = dftest.iloc[:, :-1], dftest.iloc[:, -1]
	all_X = df.iloc[:, :-1]

	# # load model
	# model = tf.keras.models.load_model('LSTM_model_' + countyName + '.h5')

	# or build model
	model = keras.Sequential()
	# Add an Embedding layer expecting input vocab of size 1000, and
	# output embedding dimension of size 64.
	model.add(layers.Embedding(input_dim=1000, output_dim=64))
	# Add a LSTM layer with 128 internal units.
	model.add(layers.LSTM(numLSTMunits))
	model.add(layers.Dense(numOutput))

	model.summary()

	model.compile(loss='mae', optimizer='adam')
	history = model.fit(train_X, train_y, epochs=maxEpochs, batch_size=batchSize, 
		validation_data=(test_X, test_y), verbose=2, shuffle=False)
	# plot history
	pyplot.plot(history.history['loss'], label='train')
	pyplot.plot(history.history['val_loss'], label='test')
	pyplot.legend()
	pyplot.savefig('LSTM_Epochs_' + countyName + '.png')
	pyplot.clf()

	# save trained model
	model.save('LSTM_model_' + countyName + '.h5')

	# make a prediction
	ypred = model.predict(all_X, verbose=0)
	# with open('LSTM_Predictions_' + countyName + '.csv', 'w') as f:
	# 	print(ypred, file=f)
	numpy.savetxt('LSTM_Predictions_' + countyName + '.csv', ypred, delimiter=",")

	if contourProcess:
		cypred = model.predict(dfContour, verbose=0)
		numpy.savetxt('LSTM_Contour_Predictions_' + countyName + '.csv', cypred, delimiter=",")