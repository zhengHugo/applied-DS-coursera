import pandas as pd

df = pd.read_csv('C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment2/olympics.csv', index_col=0, skiprows=1, encoding='utf-8')

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\\s\\(') # split the index by '('

# the [0] element is the country name (new index) 
df.index = names_ids.str[0] 

# the [1] element is the abbreviation or ID 
# (take first 3 characters from that)
df['ID'] = names_ids.str[1].str[:3] 

df = df.drop('Totals')
# print(df.head())

# Which country has won the most gold medals in summer games?
# This function should return a single string value.
def answer_one():
    max_country = ''
    max = 0
    for index, row in df.iterrows():
        if row['Gold'] > max:
            max = row['Gold']
            max_country = index
    return max_country

# print(answer_one())

# Which country had the biggest difference between their summer and winter 
# gold medal counts?
# This function should return a single string value
def answer_two():
    rt_country = ''
    max_diff = 0
    for index, row in df.iterrows():
        if abs(row['Gold'] - row['Gold.1']) > max_diff:
            max_diff = abs(row['Gold'] - row['Gold.1'])
            rt_country = index
    return rt_country

# print(answer_two())
