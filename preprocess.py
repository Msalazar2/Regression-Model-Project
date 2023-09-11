from scipy import stats
import pandas as pd


#function that changes churn values to Yes & No, and drops insignificant columns to return x and y split
def xy_split(df):
    
    return df.drop(columns= 'tax_value'), df.tax_value
    

#function applies one hot encoding to categorical feature and drops repetitave features
def dummies(train, val, test):
    
    train = pd.get_dummies(train)
    
    val = pd.get_dummies(val)
    
    test = pd.get_dummies(test)
    
    return train, val, test