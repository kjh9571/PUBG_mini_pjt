from unittest import load_tests
import pandas as pd

base_path = 'data/raw/'

df_train = pd.read_csv('train_V2.csv')
df_test = pd.read_csv('test_V2.csv')
submission = pd.read_csv('sample_submission_V2.csv')
