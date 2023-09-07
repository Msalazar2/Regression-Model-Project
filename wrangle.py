import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from env import get_connection



def get_zillow():
    
    filename = 'new_zillow.csv'
    
    if os.path.isfile(filename):
        
        print('found data')
        
        return pd.read_csv(filename)
    
    else:
        
        print('retrieving data')
        
        query = '''
                SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips, propertylandusetypeid, transactiondate
                FROM predictions_2017 AS pred
                LEFT JOIN properties_2017 AS p ON pred.parcelid = p.parcelid
                WHERE transactiondate LIKE ('2017%%')
                AND propertylandusetypeid = '261'
                ;
                '''
        
        url = get_connection('zillow')
        
        df = pd.read_sql(query, url)
        
        df.to_csv(filename, index = 0)
        
        return df

def clean_zillow():
    
    df = get_zillow()
    
    df = df.rename(columns={'bedroomcnt': 'bedrooms', 'bathroomcnt': 'bathrooms',
                            'calculatedfinishedsquarefeet': 'square_ft', 
                            'taxvaluedollarcnt': 'tax_value', 'yearbuilt': 'year',
                            'taxamount':'tax_amount'})
    
    #drop nulls
    df = df.dropna()
    
    #drop tax_amount
    df = df.drop(columns = ['tax_amount', 'propertylandusetypeid', 'transactiondate'])
    
    #cast to int
    df.tax_value = df.tax_value.astype('int')
    
    df.year = df.year.astype('int')
    
    df.square_ft = df.square_ft.astype('int')
    
    df.bedrooms = df.bedrooms.astype('int')
    
    
    
    #rename fips column and values
    df['fips'] = df['fips'].map({6037: 'Los Angeles', 6059: 'Orange', 6111: 'Ventura'})
    
    df = df.rename(columns = {'fips': 'county'})
    
    return df


def scale_data(train, val, test, to_scale):
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