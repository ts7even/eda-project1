import pandas as pd
import numpy as np 

# Datasets 
school_district_data = 'source/dataset/SASS_99_00_S1a_v1_0.csv'
public_school_principle = 'source/dataset/SASS_99_00_S2a_v1_0.csv'
private_school_principle = 'source/dataset/SASS_99_00_S2b_v1_0.csv'
public_school = 'source/dataset/SASS_99_00_S3a_v1_0.csv'
private_school = 'source/dataset/SASS_99_00_S3b_v1_0.csv'
public_teacher_data = 'source/dataset/SASS_99_00_S4a_v1_0.csv'
private_teacher_data = 'source/dataset/SASS_99_00_S4b_v1_0.csv'
former_teacher = 'source/dataset/SASS_99_00_T2_v1_0.csv'
current_teacher = 'source/dataset/SASS_99_00_T3_v1_0.csv'

# Setting up dataframe
df1 = pd.read_csv(school_district_data, low_memory=False)
df2 = pd.read_csv(public_school_principle, low_memory=False)
df3 = pd.read_csv(private_school_principle, low_memory=False)
df4 = pd.read_csv(public_school, low_memory=False)
df5 = pd.read_csv(private_school, low_memory=False)
df6 = pd.read_csv(public_teacher_data, low_memory=False)
df7 = pd.read_csv(private_teacher_data, low_memory=False)
df8 = pd.read_csv(former_teacher, low_memory=False)
df9 = pd.read_csv(current_teacher, low_memory=False)


print("There are nine datafiles in total.")

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

    t2_observation = df8.shape[0]
    t2_varible = df8.shape[1]
    print(f'Former Teacher data has {t2_observation} observations, and {t2_varible} varibles.')

    t3_observation = df9.shape[0]
    t3_varible = df9.shape[1]
    print(f'Current Teacher data has {t3_observation} observations, and {t3_varible} varibles.')
    print()

    # Control Numbers  
    print('The control number for Public Teacher Data is (CNTLNUM) and (SCHCNTL)')
    print('The control number for Public School Data is (SCHCNTL) ')
    print('The control number for Public Principle Data is (CNTLNUM) and (SCHCNTL)')
    print('The control number for Public District Data is (CNTLNUM)')
    print()


# Only working with the public teacher file df6
def publicTeacher():
    # Question 1: How many public school teachers in your dataset?
    s4a_observation = df6.shape[0]
    print('Working with the Public School Teacher File - Data Processing and Analysis')
    print('Question 1: How many public school teachers in your dataset?')
    print(f'There are {s4a_observation} public teachers.')
    print()

    # Question 2: How many of them are make teachers versus female teachers?
    male_teachers = df6[(df6["T0356"]==1)]
    total_male = male_teachers.shape[0]
    female_teacher = df6[(df6["T0356"]==2)]
    total_female = female_teacher.shape[0]
    describe_sex = df6['T0356'].describe()
    print('Question 2: How many of them are male teachers versus female teachers?')
    print(f'There are {total_male} male teachers and {total_female} female teachers.')
    print(describe_sex)
    print()

    # Question 3: How many teachers are White, Black, Hispanic, Asian, or American Indian? 
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
    describe_ethnicity = df6['RACETH_T'].describe()
    print('Question 3: How teachers are White, Black, Hispanic, Asian, or American Indian?')
    print(f'There are {total_white_teachers} White teachers.')
    print(f'There are {total_black_teachers} Black teachers.')
    print(f'There are {total_hispanic_teachers} Hispanic teachers.')
    print(f'There are {total_asian_teachers} Asian teachers.')
    print(f'There are {total_american_indian_teachers} American Indian teachers.')
    print(describe_ethnicity)
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
    describe_age = df6['AGE_T'].describe()
    print('Question 4: What is the public teachers age distribution?')
    print(f'There are {total_age_1} teachers that are 30 years old or younger.')
    print(f'There are {total_age_2} teachers that are between 30 to 39 years old.')
    print(f'There are {total_age_3} teachers that are 40 to 49 years old.')
    print(f'There are {total_age_4} teachers that are 50 years old or older.')
    print(describe_age)
    print()

    # Question 5: How many teachers are teaching elementary school, middle school, or high school?
    elementary_school = df6[ (df6['TEALEV']== 1)]
    total_elementary = elementary_school.shape[0]
    middle_school = df6[ (df6['TEALEV']== 2)]
    total_middle = middle_school.shape[0]
    high_school = df6[ (df6['TEALEV']== 3)]
    total_high = high_school.shape[0]
    other_school = df6[ (df6['TEALEV']== 4)]
    total_other = other_school.shape[0]
    describe_school = df6['TEALEV'].describe()
    print('Quesiton 5: How many teachers are teaching elementary school, middle school, or high school?')
    print(f'There are {total_elementary} elementary school teachers.')
    print(f'There are {total_middle} middle school teachers.')
    print(f'There are {total_high} high school teachers.')
    print(f'There are {total_other} "other" school teachers.')
    print(describe_school)
    print()


    # Question 6: What are the general fields of main assignment (ASSIGN)?
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
    describe_assign = df6['ASSIGN'].describe()
    print('Question 6: What are the general fields of course study/main assignment (ASSIGN)?')
    print(f'There are {total_prek} teachers that teach Pre-Kindergarten, Kindergarten, and/or General Elementary.')
    print(f'There are {total_math_science} teachers that teach mathematics and science.')
    print(f'There are {total_english_language} teachers that teach English/language arts. ')
    print(f'There are {total_social_science} teachers that teach social sciences.')
    print(f'There are {total_special_education} teachers that teach special education.')
    print(f'There are {total_forieign_language} teachers that teach foreign languages.')
    print(f'There are {total_bilingual_ESL} teachers that teach bilingual/ESL education.')
    print(f'There are {total_vocational_technical} teachers that teach vocational/technical education.')
    print(f'There are {total_all_others} teachers that teach "all other." ')
    print(describe_assign)
    print()


# Processing the Public School file...
def publicSchools():
    # Question 1: How many public schools are there in you dataset?
    total_public_schools = df4.shape[0]
    print('Processing the Public School file - DATA Processing and Analyis')
    print()
    print('Question 1: How many schools are there in your data set? ')
    print(f'There are {total_public_schools} schools in the dataset.')
    print()

    # Question 2: How many elementary schools are there in the state of Texas, in the state of California, and in the state of Florida?
    #         1 = Northeast | 2 = Midwest | 3 = South | 4 = West
    elementary_schools = df4[(df4['SCHLEVEL']==1)]
    texas_elementary_schools = df4[(df4['SCHLEVEL']==1) & (df4['REGION']== 3) ]
    total_south_elementary_schools = texas_elementary_schools.shape[0]
    ca_elementary_schools = df4[(df4['SCHLEVEL']==1) & (df4['REGION']== 4) ]
    total_west_elementary_schools = ca_elementary_schools.shape[0]
    describe_elementary_schools = elementary_schools.groupby('REGION')['REGION'].count() # There is another way to describe only elementary schools and by region by using groupby. This just gives the stats of the varibles.
    print('Question 2: How many elementary schools are there in the state of Texas, in the state of California, and in the state of Florida? ')
    print(f'Only found data according to region in the public school file, so the Southern region (Texas & Florida) has {total_south_elementary_schools} elementary schools.')
    print(f'As for the Western reigion (California) there are {total_west_elementary_schools} elementary schools.')
    print(describe_elementary_schools)
    print()


    # Question 3: What is the average enrollment size (number of students) for highschools?
    high_schools = df4[(df4['SCHLEVEL']==2)]
    total_high_schools = high_schools.shape[0]
    enrollment_size_highschool_less300 = df4[(df4['S0092']== 1) & (df4['SCHLEVEL']==2)  ] # Less that 300
    total_less_300 = enrollment_size_highschool_less300.shape[0]
    enrollment_size_highschool_300to499 = df4[(df4['S0092']== 2) & (df4['SCHLEVEL']==2) ] # Between 300 - 499
    total_300to499 = enrollment_size_highschool_300to499.shape[0]
    enrollment_size_highschool_500ormore = df4[(df4['S0092']== 3) & (df4['SCHLEVEL']==2) ] # 500 or more
    total_500ormore = enrollment_size_highschool_500ormore.shape[0]
    describe_students = high_schools[['S0092']].describe()   
    print('Question 3: What is the average enrollment size (number of students) for highschools?')
    print(f'The total amount of highschools: {total_high_schools}')
    print(f'There are {total_less_300} highschools that have less than 300 students; {round((total_less_300/total_high_schools)*100, 2)}%.')
    print(f'There are {total_300to499} highschools that have between 300 and 499 students; average {round((total_300to499/total_high_schools)*100,2)}%.')
    print(f'There are {total_500ormore} highschools that have 500 or more students; average {round((total_500ormore/total_high_schools)*100,2)}%.')
    print(describe_students)
    print()
  

    # Question 4: What is the average number of teachers in these public schools? #S0254 = Total Teachers at Schools
    teacher_size_less25 = df4[(df4['S0254']== 1) ]
    total_less25 = teacher_size_less25.shape[0]
    teacher_size_25to34 = df4[(df4['S0254']== 2) ]
    total_25to34 = teacher_size_25to34.shape[0]
    teacher_size_35ormore = df4[(df4['S0254']== 3) ]
    total_35ormore = teacher_size_35ormore.shape[0]
    describe_teachers = df4['S0254'].describe()
    print('Question 4: What is the average number of teachers in these public schools? #S0254 = Total Teachers at Schools')
    print(f'There are {total_less25} schools with less than 25 teachers.')
    print(f'There are {total_25to34} schools that have between 25 and 34 teachers. ')
    print(f'There are {total_35ormore} schools with more than 35 teachers.')
    print(describe_teachers)
    print()

    # Question 5: What is the average number of students eligible for the free/reduced lunch program? #S0284 = eligible lunch
    valid_skip = df4[(df4['S0284']!= -8)]
    less_than_five_percent = df4[(df4['S0284']== 1)]
    total_less_than_five_percent = less_than_five_percent.shape[0]
    between_five_and_19_percent = df4[(df4['S0284']== 2)]
    total_between_five_and_19_percent = between_five_and_19_percent.shape[0]
    between_20_and_49_percent = df4[(df4['S0284']== 3)]
    total_between_20_and_49_percent = between_20_and_49_percent.shape[0]
    fifty_percent_or_more = df4[(df4['S0284']== 4)]
    total_fifty_percent_or_more = fifty_percent_or_more.shape[0]
    describe_lunch_no_valid = valid_skip[['S0284']].describe()
    describe_lunch_with_valid = df4['S0284'].describe()
    print('Question 5: What is the average number of students eligible for the free/reduced lunch program?')
    print(f'Provided two different summary stats. One without the valid skip, and one that includes valid skip. ')
    print(f'The amount of students that are eligible for free lunch. (Less than 5%): {total_less_than_five_percent}')
    print(f'The amount of students that are eligible for free lunch. (Between 5% and 19%): {total_between_five_and_19_percent} ')
    print(f'The amount of students that are eligible for free lunch. (Between 20% and 49%): {total_between_20_and_49_percent} ')
    print(f'The amount of students that are eligible for free lunch. (50% or more): {total_fifty_percent_or_more}')
    print()
    print('The summary stats without the valid skip.')
    print(describe_lunch_no_valid)
    print()
    print('The summary stats that includes the valid skip option.')
    print(describe_lunch_with_valid)
summary_dataset()
publicTeacher()
publicSchools()

