import pandas as pd
import numpy as np 
from pandas_profiling import ProfileReport
import time
start =time.time()
# Summary stats using pandas-profile library pip install pandas-profiling. Has to be pandas version 1.3.5


def summary():
    df4 = pd.read_csv('source/dataset/SASS_99_00_S3a_v1_0.csv', low_memory=False)
    df6 = pd.read_csv('source/dataset/SASS_99_00_S4a_v1_0.csv', low_memory=False)

    public_school_profile = ProfileReport(df4, title='Public School Summary Statistics', minimal=True)
    public_teacher_profile = ProfileReport(df6, title='Public Teacher Summary Statistics', minimal=True)

    public_school_profile.to_file('Resources/publicSchoolMerge.html')
    public_teacher_profile.to_file('Resources/publicTeacherMerge.html')
summary()    
print(f'It took: {time.time()-start} seconds...')