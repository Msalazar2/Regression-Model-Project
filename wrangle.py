import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

from env import get_connection
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.model_selection import train_test_split



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
                            'taxamount':'tax_amount', 'fips': 'county', 'propertylandusetypeid': 'property_type',
                            'transactiondate': 'transaction_date'})
    
    #drop nulls
    df = df.dropna()
    
    
    #drop duplicates
    df = df.drop_duplicates(subset=['square_ft', 'year', 'tax_amount', 'county',
                                    'transaction_date', 'tax_value', 'bedrooms', 'bathrooms'], keep = 'first')
    
    #drop 0 values for bedrooms and bathrooms
    df = df[df.bedrooms != 0]
    
    df = df[df.bathrooms != 0]
   
    #drop tax_amount
    df = df.drop(columns = ['tax_amount', 'property_type', 'transaction_date'])
    
    #cast to int
    df.tax_value = df.tax_value.astype('int')
    
    df.year = df.year.astype('int')
    
    df.square_ft = df.square_ft.astype('int')
    
    df.bedrooms = df.bedrooms.astype('int')
    
    
    
    #rename fips column and values
    df['county'] = df['county'].map({6037: 'Los Angeles', 6059: 'Orange', 6111: 'Ventura'})
 
    
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



def split_data(df):

    seed = 42

    train, val_test = train_test_split(df, train_size = .7,
                                        random_state = seed)

    val, test = train_test_split(val_test, train_size = .5,
                                random_state = seed)

    return train, val, test



def r_scaler(df, features):

    rs = RobustScaler()

    rs.fit(df[features])

    df[['bedrooms_rs','bathrooms_rs','square_ft_rs','tax_value_rs','year_rs','tax_amount_rs']] = rs.transform(df[features])

    return df