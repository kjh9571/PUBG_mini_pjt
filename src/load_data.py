import pandas as pd

def load_train(base_path):
    base_path = base_path
    df_train = pd.read_csv(base_path + 'train_V2.csv')
    return df_train

def load_test(base_path):
    base_path = base_path
    df_test = pd.read_csv(base_path + 'test_V2.csv')
    return df_test    
    
