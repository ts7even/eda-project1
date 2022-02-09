import pandas as pd
import numpy as np


# The assignment Merge 
df1 = pd.read_csv('source/dataset/SASS_99_00_S3a_v1_0.csv')
df2 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv')

# Trying to Merge Public and Private teacher for test 
df3 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv')
df4 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv')


# test mockup of merge 

data_merge1 = pd.merge(df1, df2, how='inner') # Inner means intersection - Outer means Union. This is trying to merge on columns. 
data_merge2 = pd.merge(df2, df3,  how='inner')
data_merge3 = pd.merge(df1, df2, how='inner', validate='m:m')

# data_merge1 = True if data_merge_shape1 is >= 1:

data_merge_shape1 = data_merge1.shape[0]
data_merge_shape2 = data_merge2.shape[0]
data_merge_shape3 = data_merge3.shape[0]


shape1 = df1.shape[1]
shape2 = df2.shape[1]
total_shape_varibles = np.sum(shape1 + shape2)



def dataMerge():
    print(f'df1 has {shape1} columns and df2 has {shape2} columns. Total from both datasets are: {total_shape_varibles}  '   )
    if data_merge_shape1 >=1: # Tryed to do >=1 instead of a boolean
        return print(f'The data tried to merge a relationship. Number of observations that merged {data_merge_shape1}')

    elif data_merge_shape2 >=1: # Tryed to do >=1 instead of a boolean
        return print(f'The data tried to merge a relationship between public and private teacher data. Number of observations that merged {data_merge_shape2} ')

    elif data_merge_shape3 >=1: # Tryed to do >=1 instead of a boolean
        return print(f'The data tried to merge a relationship. Number of observations that merged {data_merge_shape3} ')

    else:
        return print('Non of the merged solutions worked since there is no intersection of varibles. ')

dataMerge()


