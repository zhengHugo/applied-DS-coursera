import pandas as pd

census_df = pd.read_csv('C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment2/census.csv')
# print(census_df.head())
# print(census_df.loc[:,['SUMLEV', 'STATE', 'COUNTY']])

'''
    Which state has the most counties in it? (hint: consider the sumlevel key
    carefully! You'll need this for future questions too...)
    This function should return a single string value
'''
def answer_five():
    states = census_df['STNAME'].unique()
    # print(states)
    # print(census_df['STNAME'])
    county_num = pd.Series([0] * len(states), index = states)
    for country in census_df.iterrows():
        if country[1]['SUMLEV'] == 40:
            continue
        county_num[country[1]['STNAME']] += 1
    return county_num.idxmax()
print(answer_five())


