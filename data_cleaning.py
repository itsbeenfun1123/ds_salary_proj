# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:16:41 2020

@author: benfa
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x : x.split('(')[0])
minus_Kd = salary.apply(lambda x : x.replace('K','').replace('$',''))

df['min_salary'] = minus_Kd.apply(lambda x : int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x : int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

# company name text only
df['company_txt'] = df.apply(lambda x : x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

# state field
df['job_state'] = df['Location'].apply(lambda x : x.split(',')[1] if ',' in x else '')
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x : 1 if x.Location == x.Headquarters else 0, axis = 1)
# age of company
df['age'] = df.Founded.apply(lambda x : x if x < 1 else 2020 - x)

# parsing of job description

df['python_yn'] = df['Job Description'].apply(lambda x : 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

df['R_yn'] = df['Job Description'].apply(lambda x : 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

df['spark'] = df['Job Description'].apply(lambda x : 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

df['aws'] = df['Job Description'].apply(lambda x : 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

df['excel'] = df['Job Description'].apply(lambda x : 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

df.to_csv('salary_data_cleaned.csv')

