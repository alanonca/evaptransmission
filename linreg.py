import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table
import numpy as np
from statsmodels.sandbox.regression.predstd import wls_prediction_std

def trainTestSplit(df, lastxRowForTest, filename=None, contourProcess = False, dfContour = None):
    df = sm.add_constant(df) # adding a constant

    # creating training and testing datasets
    dftrain = df.head(df.shape[0]-lastxRowForTest)
    dftest = df.tail(lastxRowForTest)

    # print(df)
    # print(dftest)

    Xtrain = dftrain.iloc[:,:-1]
    Ytrain = dftrain.iloc[:,-1]
    Xtest = dftest.iloc[:,:-1]
    Ytest = dftest.iloc[:,-1]
    Xall = df.iloc[:,:-1]
    
    # train
    model = sm.OLS(Ytrain, Xtrain).fit()
    print_model = model.summary().as_csv()
    print(print_model)

    # test
    predictions = model.predict(Xtest) 
    print("Testing actual vs predicted:")
    print("Actual:")
    print(Ytest)
    print(":Predicted:")
    print(predictions)

    # get prediction interval for all Xs
    # predictions2 = model.get_prediction(Xtest)
    # print(predictions2.summary_frame(alpha=0.05))
    predictions2 = model.get_prediction(Xall)
    predictions2df = predictions2.summary_frame(alpha=0.17)
    print(predictions2df)

    # write to filename
    f = open(filename+"_ARLR_SummaryTable.csv", "w")
    f.write(print_model)
    f.close()
    predictions2df.to_csv(filename+"_ARLR_Predictions.csv")

    # print(Xall.shape)
    # print(dfContour.shape)

    if contourProcess:
        dfContour = sm.add_constant(dfContour)
        predictions3 = model.get_prediction(dfContour)
        predictions3df = predictions3.summary_frame(alpha=0.17)
        predictions3df.to_csv(filename+"_ARLR_Contour_Predictions.csv")

def regOnly(df):
    df = sm.add_constant(df) # adding a constant
    X = df.iloc[:,:-1]
    Y = df.iloc[:,-1]

    model = sm.OLS(Y, X).fit()
    print_model = model.summary()
    print(print_model)