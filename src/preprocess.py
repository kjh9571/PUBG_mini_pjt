from load_data import df_train

train = df_train

# 결측치 확인
print(train[train.isnull().any(axis=1)])

# 결측치 제거
# df_train.dropna(axis=1)
