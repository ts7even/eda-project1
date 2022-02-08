import pandas as pd
import numpy as np

public_school = 'source/dataset/SASS_99_00_S3a_v1_0.csv'
public_teacher = 'source/dataset/SASS_99_00_S4a_v1_0.csv'

df1 = pd.read_csv('source/dataset/SASS_99_00_S3a_v1_0.csv')
df2 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv')


data_merge = pd.merge(df1, df2)
data_merge.head(10)





# data_concat = pd.concat(public_school, public_teacher)

# df = data_merge.to_csv("data_merge.csv", index=False)

# print(' Merged To CSV File ')
