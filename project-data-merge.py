import pandas as pd
import numpy as np
import sys

# To remove traceback and to only get an error. Needed to import sys
sys.tracebacklimit = 0

public_school = 'source/dataset/SASS_99_00_S3a_v1_0.csv'
public_teacher = 'source/dataset/SASS_99_00_S4a_v1_0.csv'

df1 = pd.read_csv('source/dataset/SASS_99_00_S3a_v1_0.csv')
df2 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv')

data_merge = df2.merge(df1, how='inner') # Inner means intersection - Outer means Union
# data_1_to_many = df2.merge(df1,  validate='1:m')
# data_many_to_many = df2.merge(df1, validate='m:1')

data_merge_shape = data_merge.shape[1]

print(f'Only {data_merge_shape} varibles merged.')


# print(data_1_to_many)
# print(data_many_to_many)

# It will return:  pandas.errors.MergeError: Merge keys are not unique in left dataset; not a one-to-one merge
# But we need to find and print how many of them correctly merged and how many failed to merge. 



