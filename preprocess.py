from scipy import stats
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler



def xy_split(df):
    '''
    This function splits your data for modeling. 
    
    Parameter: 
    df = data
    
    Output:
    This function returns subsets of your data. One with all columns except your target variable, and the other with only the target variable.
    '''
    
    return df.drop(columns= 'tax_value'), df.tax_value
    


def dummies(train, val, test):
    '''
    This function applies one hot encoding to all categorical features in your dataset.
    
    Parameters:
    train = train data
    val = val data
    test = test data
    
    Output:
    This function returns your train, val, and test subsets with dummies added.
    '''
    
    train = pd.get_dummies(train)
    
    val = pd.get_dummies(val)
    
    test = pd.get_dummies(test)
    
    return train, val, test


def scale_data(train, val, test, to_scale):
    '''
    This function scales all continuous numerical features in your train, val, and test subsets.
    
    Parameters:
    train = train data
    val = val data
    test = test data
    to_scale = features to scale
    
    Output:
    This function returns scaled features added to your data.
    '''
    #make copies for scaling
    train_scaled = train.copy()
    validate_scaled = val.copy()
    test_scaled = test.copy()

    #make the thing
    scaler = MinMaxScaler()

    #fit the thing
    scaler.fit(train[to_scale])

    #use the thing
    train_scaled[to_scale] = scaler.transform(train[to_scale])
    validate_scaled[to_scale] = scaler.transform(val[to_scale])
    test_scaled[to_scale] = scaler.transform(test[to_scale])
    
    return train_scaled, validate_scaled, test_scaled
