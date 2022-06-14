import pandas as pd

def matchType_classify(df):
    def classify(x):
        if 'flare' in x or 'crash' in x or 'normal' in x:
            return 'custom'
        elif 'solo' in x:
            return 'solo'
        elif 'duo' in x:            
            return 'duo'
        else: 
            return 'squad'
    
    new_df = df
    new_df['matchType'] = df['matchType'].apply(classify)
    return new_df

def matchType_encoding(df):
    df_OHE = pd.get_dummies(df, columns=['matchType'])
    return df_OHE

def average_speed(df):
    return 0