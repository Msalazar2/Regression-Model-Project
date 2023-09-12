import pandas as pd
import seaborn as sns
import os


from sklearn.model_selection import train_test_split
from env import get_connection



def get_zillow():
    '''
    This function aquires the appropriate data for the project from MySQL. All you have to do is assign the function to a variable to read in the data.
    ex: df = get_zillow
    '''
    
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
    '''
    This function calls the get_zillow() function and prepares the data for training. All you have to do is assign this function to a variable to acquire the prepped data.
    ex: df = clean_zillow()
    '''
    
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
   
    #drop tax_amount and other insignificant features
    df = df.drop(columns = ['tax_amount', 'property_type', 'transaction_date'])
    
    #cast to int
    df.tax_value = df.tax_value.astype('int')
    
    df.year = df.year.astype('int')
    
    df.square_ft = df.square_ft.astype('int')
    
    df.bedrooms = df.bedrooms.astype('int')
    
    #rename fips column and values
    df['county'] = df['county'].map({6037: 'Los Angeles', 6059: 'Orange', 6111: 'Ventura'})
    
    return df



def split_data(df):
    '''
    This function uses your dataframe and calls the train_test_split function from sklearn and assigns the output to the train, validate, and test subsets.

    Parameters: 
    df = data
    '''
    seed = 42

    train, val_test = train_test_split(df, train_size = .7,
                                        random_state = seed)
    val, test = train_test_split(val_test, train_size = .5,
                                random_state = seed)
    return train, val, test



def bin_data(df):
    '''
    This function bins specific continuous features and creates new columns for them. This will be useful when creating visuals.
    
    Parameters:
    df = data
    '''
    
    #bin data
    bin_bound = [0, 1.9, 2.9, 3.9, 4.9, 5.9, 18]

    bin_labels = [1, 2, 3, 4, 5, 18]

    df['bathrooms_bin'] = pd.cut(df['bathrooms'], bins = bin_bound, labels = bin_labels)
     
    
    bin_bound = [0, 1.9, 2.9, 3.9, 4.9, 5.9, 6.9, 14]

    bin_labels = [1, 2, 3, 4, 5, 6, 14]

    df['bedrooms_bin'] = pd.cut(df['bedrooms'], bins = bin_bound, labels = bin_labels)

    
    bin_bound = [0, 1000, 1500, 2000, 2500, 3000, 3500, 21929]

    bin_labels = [1000, 1500, 2000, 2500, 3000, 3500, 21929]

    df['square_ft_bin'] = pd.cut(df['square_ft'], bins = bin_bound, labels = bin_labels)
   
    
    bin_bound = [0, 1959, 1969, 1979, 1989, 1999, 2009, 2020 ]

    bin_labels = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

    df['decade'] = pd.cut(df['year'], bins = bin_bound, labels = bin_labels)
    
    #create column
    df['total_rooms'] = df.bedrooms + df.bathrooms
    
    bin_bound = [0, 3.9, 4.9, 5.9, 6.9, 33]

    bin_labels = [3, 4, 5, 6, 32]

    df['total_rooms_bin'] = pd.cut(df['total_rooms'], bins = bin_bound, labels = bin_labels)
    
    return df
