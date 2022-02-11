import pandas as pd
import numpy as np





# The assignment Merge 
df1 = pd.read_csv('source/dataset/SASS_99_00_S3a_v1_0.csv') # Public School Control Numbers is (SCHCNTL - School Control Number)
df2 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv') # Public School Teachers (CNTLNUM- Disctric) and (SCHCNTL - School Control Number)




# Concat Test Mockup 


def dataMerge():
    merge_test_1 = pd.merge(df1, df2, on="SCHCNTL")
    merge_shape_1 = merge_test_1.shape[0]
    print(merge_test_1)
    print()
    print(f'The amount of observations that merged {merge_shape_1}')
dataMerge()



