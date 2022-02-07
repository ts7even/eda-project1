import pandas as pd
import numpy as np 


# All you need to do is to provide the correct path for the 
# Datasets 
school_district_data = 'source/dataset/SASS_99_00_S1a_v1_0.csv'
public_school_principle = 'source/dataset/SASS_99_00_S2a_v1_0.csv'
private_school_principle = 'source/dataset/SASS_99_00_S2b_v1_0.csv'
public_school = 'source/dataset/SASS_99_00_S3a_v1_0.csv'
private_school = 'source/dataset/SASS_99_00_S3b_v1_0.csv'
public_teacher_data = 'source/dataset/SASS_99_00_S4a_v1_0.csv'
private_teacher_data = 'source/dataset/SASS_99_00_S4b_v1_0.csv'

idk_what_this_is1 = 'source/dataset/SASS_99_00_T2_v1_0.csv'
idk_what_this_is2 = 'source/dataset/SASS_99_00_T3_v1_0.csv'

# Setting up dataframe
df1 = pd.read_csv(school_district_data, low_memory=False)
df2 = pd.read_csv(public_school_principle, low_memory=False)
df3 = pd.read_csv(private_school_principle, low_memory=False)
df4 = pd.read_csv(public_school, low_memory=False)
df5 = pd.read_csv(private_school, low_memory=False)
df6 = pd.read_csv(public_teacher_data, low_memory=False)
df7 = pd.read_csv(private_teacher_data, low_memory=False)
df8 = pd.read_csv(idk_what_this_is1, low_memory=False)
df9 = pd.read_csv(idk_what_this_is2, low_memory=False)


# print("There are nine datafiles in total.")

# Summary Statistics for all files in the dataset
# .shape[0] = Observations
# .shape[1] = Varibles
print()
def summary_dataset():
    s1a_observation = df1.shape[0] #Observations
    s1a_varible = df1.shape[1] #Varibles
    print(f'School District Data has {s1a_observation} observations, and {s1a_varible} varibles.')

    s2a_observation = df2.shape[0]
    s2a_varible = df2.shape[1]
    print(f'Public School Principle Data has {s2a_observation} observations, and {s2a_varible} varibles.')

    s2b_observation = df3.shape[0]
    s2b_varible = df3.shape[1]
    print(f'Private School Principle Data has {s2b_observation} observations, and {s2b_varible} varibles.')

    s3a_observation = df4.shape[0]
    s3a_varible = df4.shape[1]
    print(f'Public School data has {s3a_observation} observations, and {s3a_varible} varibles.')

    s3b_observation = df5.shape[0]
    s3b_varible = df5.shape[1]
    print(f'Private School data has {s3b_observation} observations, and {s3b_varible} varibles.')

    s4a_observation = df6.shape[0]
    s4a_varible = df6.shape[1]
    print(f'Public Teacher data has {s4a_observation} observations, and {s4a_varible} varibles.')

    s4b_obervation = df7.shape[0]
    s4b_varible = df7.shape[1]
    print(f'Private Teacher data has {s4b_obervation} observations, and {s4b_varible} varibles.')

    t1_observation = df8.shape[0]
    t1_varible = df8.shape[1]
    print(f'T1 has {t1_observation} observations, and {t1_varible} varibles.')

    t2_observation = df9.shape[0]
    t2_varible = df9.shape[1]
    print(f'T2 has {t2_observation} observations, and {t2_varible} varibles.')
    print()

    # Control Numbers and I dont think these are right. 
    print('The control number for Public Teacher Data is (CNTLNUM) and (SCHCNTL)')
    print('The control number for Public School Data is (SCHCNTL) ')
    print('The control number for Public Principle Data is (CNTLNUM) and (SCHCNTL)')
    print('The control number for Public Distric Data is (CNTLNUM)')
    print()


# only working with the public teacher file df6
def publicTeacher():
    # Question 1: How many public school teachers in your dataset?
    s4a_observation = df6.shape[0]
    print('Working with the Public School Teacher File - Data Processing and Analysis')
    print('Question 1: How many public school teachers in your dataset?')
    print(f'There are {s4a_observation} public teachers ')
    print()

    # Question 2: How many of them are make teachers versus female teachers?
    male_teachers = df6[(df6["T0356"]==1)]
    total_male = male_teachers.shape[0]
    female_teacher = df6[(df6["T0356"]==2)]
    total_female = female_teacher.shape[0]
    print('Question 2: How many of them are make teachers versus female teachers?')
    print(f'There are {total_male} male teachers and {total_female} female teachers')
    print()

    # Question 3: How many of them are white, black, hispanic teachers? 
    white_teachers = df6[(df6["RACETH_T"]==4)]
    total_white_teachers = white_teachers.shape[0]
    black_teachers = df6[(df6["RACETH_T"]==3)]
    total_black_teachers = black_teachers.shape[0]
    hispanic_teachers = df6[(df6["RACETH_T"]==5)]
    total_hispanic_teachers = hispanic_teachers.shape[0]
    asian_teachers = df6[(df6["RACETH_T"]==2)]
    total_asian_teachers = asian_teachers.shape[0]
    american_indian_teachers = df6[(df6["RACETH_T"]==1)]
    total_american_indian_teachers = american_indian_teachers.shape[0]
    print('Question 3: How many of them are white, black, hispanic teachers?')
    print(f'There are {total_white_teachers} white teachers')
    print(f'There are {total_black_teachers} black teachers')
    print(f'There are {total_hispanic_teachers} hispanic teachers')
    print(f'There are {total_asian_teachers} asian teachers')
    print(f'There are {total_american_indian_teachers} american indian teachers')
    print()

    # Question 4: What is the public teachers age distribution? 
    data_age_1 = df6[ (df6['AGE_T']== 1)]
    total_age_1 = data_age_1.shape[0]
    data_age_2 = df6[ (df6['AGE_T']== 2)]
    total_age_2 = data_age_2.shape[0]
    data_age_3 = df6[ (df6['AGE_T']== 3)]
    total_age_3 = data_age_3.shape[0]
    data_age_4 = df6[ (df6['AGE_T']== 4)]
    total_age_4 = data_age_4.shape[0]
    print('Question 4: What is the public teachers age distribution?')
    print(f'There are {total_age_1} teachers that are 30 years or younger old')
    print(f'There are {total_age_2} teachers that are between 30 to 39 years old')
    print(f'There are {total_age_3} teachers that are 40 to 49 years old')
    print(f'There are {total_age_4} teachers that are 50+ years old')
    print()

    # Quesiton 5: How many teachers are teaching elementary school, middle school, and high school?
    elementary_school = df6[ (df6['TEALEV']== 1)]
    total_elementary = elementary_school.shape[0]
    middle_school = df6[ (df6['TEALEV']== 2)]
    total_middle = middle_school.shape[0]
    high_school = df6[ (df6['TEALEV']== 3)]
    total_high = high_school.shape[0]
    other_school = df6[ (df6['TEALEV']== 4)]
    total_other = other_school.shape[0]
    print('Quesiton 5: How many teachers are teaching elementary school, middle school, and high school?')
    print(f'There are {total_elementary} elementary school teachers')
    print(f'There are {total_middle} middle school teachers')
    print(f'There are {total_high} high school teachers')
    print(f'There are {total_other} "other" school teachers')
    print()


    # Question 6: What are the general fields of main assignment(ASSIGN)?
    prek_kinder_genelm = df6[ (df6['ASSIGN']== 1)]
    total_prek = prek_kinder_genelm.shape[0]
    math_science = df6[ (df6['ASSIGN']== 2)]
    total_math_science = math_science.shape[0]
    english_language = df6[ (df6['ASSIGN']== 3)]
    total_english_language = english_language.shape[0]
    social_sciences = df6[ (df6['ASSIGN']== 4)]
    total_social_science = social_sciences.shape[0]
    special_education = df6[ (df6['ASSIGN']== 5)]
    total_special_education = special_education.shape[0]
    forieign_languages = df6[ (df6['ASSIGN']== 6)]
    total_forieign_language = forieign_languages.shape[0]
    bilingual_ESL = df6[ (df6['ASSIGN']== 7)]
    total_bilingual_ESL = bilingual_ESL.shape[0]
    vocational_technical = df6[ (df6['ASSIGN']== 8)]
    total_vocational_technical = vocational_technical.shape[0]
    all_others = df6[ (df6['ASSIGN']== 9)]
    total_all_others = all_others.shape[0]
    print('Question 6: What are the general fields of main assignment(ASSIGN)?')
    print(f'There are {total_prek} teachers that teach Prekindergarten, Kindergarten, and General Elementary')
    print(f'There are {total_math_science} teachers that teach Math and Science')
    print(f'There are {total_english_language} teachers that teach English/language arts ')
    print(f'There are {total_social_science} teachers that teach Social Sciences')
    print(f'There are {total_special_education} teachers that teach Special Education')
    print(f'There are {total_forieign_language} teachers that teach Foreign Languages')
    print(f'There are {total_bilingual_ESL} teachers that teach Bilingual/ESL education')
    print(f'There are {total_vocational_technical} teachers that teach Vocational/technical education')
    print(f'There are {total_all_others} teachers that teach "All Other" ')
    print()





# Processing the Public School file - Need help for this one...
def publicSchools():
    # Question 1: How many public schools are there in you dataset?
    total_public_schools = df4.shape[0]
    print('Processing the Public School file - DATA Processing and Analyis')
    print()
    print('Question 1: How many schools are there in your data set? ')
    print(f'There are {total_public_schools} schools in the dataset')
    print()

    # Question 2: How many public schools aare there in the state of Texas, California and Florida 
    texas_elementary_schools = df4[(df4['SCHLEVEL']==1) & (df4['REGION']== 3) ]
    total_south_elementary_schools = texas_elementary_schools.shape[0]
    ca_elementary_schools = df4[(df4['SCHLEVEL']==1) & (df4['REGION']== 4) ]
    total_west_elementary_schools = ca_elementary_schools.shape[0]
    print('Question 2: How many public schools aare there in the state of Texas, California and Florida')
    print(f'Found only data by region, so the southern region has {total_south_elementary_schools} elementary schools')
    print(f'For the Western reigion (California) there are {total_west_elementary_schools} elementary schools')
    print()

    # Question 3: What is the average enrollment size (# of students) for highschools
    enrollment_size_highschool_less300 = df4[(df4['S0092']== 1) ] # Less that 300
    total_less_300 = enrollment_size_highschool_less300.shape[0]
    enrollment_size_highschool_300to499 = df4[(df4['S0092']== 2) ] # Between 300 - 499
    total_300to499 = enrollment_size_highschool_300to499.shape[0]
    enrollment_size_highschool_500ormore = df4[(df4['S0092']== 3) ] # 500 or more
    total_500ormore = enrollment_size_highschool_500ormore.shape[0]
    describe_students = df4['S0092'].describe()
    print('Question 3: What is the average enrollment size (# of students) for highschools')
    print(f'There are {total_less_300} highschools that have less than 300 students')
    print(f'There are {total_300to499} highschools that have between 300 - 499 students ')
    print(f'There are {total_500ormore} highschools that have 500 or more students')
    print(describe_students)
    print()
    # Need to use pandas summary statistics to get average

    # Question 4: What is the average number of teachers in these public schools? #S0254 = Total Teachers at Schools
    teacher_size_less25 = df4[(df4['S0254']== 1) ]
    total_less25 = teacher_size_less25.shape[0]
    teacher_size_25to34 = df4[(df4['S0254']== 2) ]
    total_25to34 = teacher_size_25to34.shape[0]
    teacher_size_35ormore = df4[(df4['S0254']== 3) ]
    total_35ormore = teacher_size_35ormore.shape[0]
    describe_teachers = df4['S0254'].describe()
    print('Question 4: What is the average number of teachers in these public schools? #S0254 = Total Teachers at Schools')
    print(f'There are {total_less25} schools with less than 25 teachers')
    print(f'There are {total_25to34} schools between 25 - 34 teachers ')
    print(f'There are {total_35ormore} schools with more than 35 teachers')
    print(describe_teachers)
    print()

    # Question 5: What is the average number of students eligible for the free lunch program? #S0282 = eligible lunch
    yes_lunch = df4[(df4['S0282']== 1)]
    total_yes_lunch = yes_lunch.shape[0]
    nope_lunch = df4[(df4['S0282']== 2)]
    total_nope_lunch = nope_lunch.shape[0]
    dont_know_lunch = df4[(df4['S0282']== 3)]
    total_dont_know = dont_know_lunch.shape[0]
    describe_lunch = df4['S0282'].describe()
    print('Question 5: What is the average number of students eligible for the free lunch program?')
    print(f'There are {total_yes_lunch} of students who are eligible for free lunch ')
    print(f'There are {total_nope_lunch} of students who are not eligible for free lunch ')
    print(f'There are {total_dont_know} students that dont know if they are eligible ')
    print(describe_lunch)
    print()





summary_dataset()
publicTeacher()
publicSchools()