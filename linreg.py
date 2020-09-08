import pandas as pd
import statsmodels.api as sm

def trainTestSplit(df, lastxRowForTest, filename=None):
    df = sm.add_constant(df) # adding a constant

    # creating training and testing datasets
    dftrain = df.head(df.shape[0]-lastxRowForTest)
    dftest = df.tail(lastxRowForTest)

    Xtrain = dftrain.iloc[:,:-1]
    Ytrain = dftrain.iloc[:,-1]
    Xtest = dftest.iloc[:,:-1]
    Ytest = dftest.iloc[:,-1]
    
    # train
    model = sm.OLS(Ytrain, Xtrain).fit()
    print_model = model.summary().as_csv()
    print(print_model)

    # write to filename
    f = open(filename+"ARLRoutput.csv", "w")
    f.write(print_model)
    f.close()

    # test
    predictions = model.predict(Xtest) 
    print("Testing actual vs predicted:")
    print("Actual:")
    print(Ytest)
    print(":Predicted:")
    print(predictions)

def regOnly(df):
    df = sm.add_constant(df) # adding a constant
    X = df.iloc[:,:-1]
    Y = df.iloc[:,-1]

    model = sm.OLS(Y, X).fit()
    print_model = model.summary()
    print(print_model)