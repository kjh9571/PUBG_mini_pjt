import pandas as pd

base_path = 'data/'

df_train = pd.read_csv(base_path + 'train_V2.csv')
df_test = pd.read_csv(base_path + 'test_V2.csv')
submission = pd.read_csv(base_path + 'sample_submission_V2.csv')