import pandas as pd
import numpy as np
 
 
# Dataframe
df6 = pd.read_csv('source\dataset\SASS_99_00_S4a_v1_0.csv', low_memory=False)
 
# T0330 - Problem-drug abuse.  
# To what extent is each of the following a problem in this school?  Student drug abuse
# 1 = Serious Problem
# 2 = Moderate Problem
# 3 = Minor Problem
# 4 = Not a problem
 
def drugAbuse():
    serious_drug_problem = df6[  (df6['T0330']==1)  ]
    total_serious_drug_problem = serious_drug_problem.shape[0]
 
    moderate_drug_problem = df6[  (df6['T0330']==2)  ]
    total_moderate_drug_problem = moderate_drug_problem.shape[0]
 
    minor_drug_problem = df6[  (df6['T0330']==3)  ]
    total_minor_drug_problem = minor_drug_problem.shape[0]
 
    not_a_drug_problem = df6[  (df6['T0330']==4)  ]
    total_not_a_drug_problem = not_a_drug_problem.shape[0]
 
    sum_of_student_drug_abuse = np.sum(total_serious_drug_problem + total_moderate_drug_problem + total_minor_drug_problem + total_not_a_drug_problem)
    summay_of_student_drug_abuse = df6['T0330'].describe()
 
    print('To what extent is there a drug problem with students at your school?')
    print(f'The total amount of reported drug abuse that is serious: {total_serious_drug_problem}')
    print(f'The total amount of reported drug abuse that is moderate: {total_moderate_drug_problem}')
    print(f'The total amount of reported drug abuse that is minor: {total_minor_drug_problem}')
    print(f'The total amount of reported drug abuse that is not a drug problem: {total_not_a_drug_problem}')
    print(f'To verify the sum of all reported drug abuse problems at school: {sum_of_student_drug_abuse}')
    print(summay_of_student_drug_abuse)
    print()
 
 
 
# T0329 - Alchol Abuse Problem
# 1 = "Serious Problem"
# 2 = "Moderate Problem"
# 3 = "Minor Problem"
# 4 = "Not a Problem"
 
def alcoholAbuse():
    serious_problem_alcohol = df6[  (df6['T0329']== 1)]
    total_serious_problem = serious_problem_alcohol.shape[0]
    moderate_problem = df6[(df6['T0329']==2)]
    total_moderate_problem = moderate_problem.shape[0]
    minor_problem = df6[(df6['T0329']== 3)]
    total_minor_problem = minor_problem.shape[0]
    not_a_problem = df6[(df6['T0329']== 4)]
    total_not_a_problem = not_a_problem.shape[0]
    verify_alcohol_stats = np.sum(total_serious_problem + total_moderate_problem + total_minor_problem + total_not_a_problem)
    summary_alcohol = df6['T0329'].describe()
 
    print('To what extent is each of the following a problem in this school?  Indicate whether it is a serious problem, a moderate problem, a minor problem, or not a problem in this school. i. Student use of alcohol')
    print(f'Total extent of alcohol that have the school has of stundents: {total_serious_problem}')
    print(f'Total teachers that have a moderate alcohol problem: {total_moderate_problem}')
    print(f'Total teachers that have a minor alcohol problem {total_minor_problem}')
    print(f'Total teachers that do not have a alcohol problem {total_not_a_problem}')
    print(f'To verify the sum of all responses in the varible "Alcohol Problem": {verify_alcohol_stats}')
    print(summary_alcohol)
    print()
 
 
drugAbuse()
alcoholAbuse()