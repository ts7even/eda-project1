import pandas as pd
import numpy as np


# The assignment Merge 
df1 = pd.read_csv('source/dataset/SASS_99_00_S3a_v1_0.csv') # Public School Control Numbers is (SCHCNTL - School Control Number)
df2 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv') # Public School Teachers (CNTLNUM- Disctric) and (SCHCNTL - School Control Number)

observation_for_public_school = df1.shape[0]
obeservaiton_for_public_teacher = df2.shape[0]
print(f'The observation number for the public school file is: {observation_for_public_school}')
print(f'The observation number for the public teacher data is: {obeservaiton_for_public_teacher}')
print

# The data merge on "SCHNTL" which is the unique identitfier for both Public Schools and Public Teachers 
def dataMerge():
    merge_test_1 = pd.merge(df1, df2, on="SCHCNTL")
    merge_shape_1 = merge_test_1.shape[0]
    print()
    print(f'The amount of observations that merged with the unique identifier "SCHCNTL": {merge_shape_1}')
dataMerge()



# Identify why some of the observations did not merge. 
# It is becuase those observations corrisond with a different unique identifer which is not included in public school 
# Therefore there is not a 1 to 1 relationship or a 1 to many relationship.  