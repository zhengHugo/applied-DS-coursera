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
    county_num = pd.Series([0] * len(states), index = states)
    for country in census_df.iterrows():
        if country[1]['SUMLEV'] == 40:
            continue
        county_num[country[1]['STNAME']] += 1
    return county_num.idxmax()

# print(answer_five())

'''
    Only look at the three most populous counties for each state 
    What are the three most populous states (in order of highest population to
    lowest population)? Use CENSUS2010POP.
'''
def answer_six():
    counties_df = census_df.where(census_df['SUMLEV'] == 50)
    top_counties_df = counties_df.sort_values(by = 'CENSUS2010POP', ascending  = False).groupby('STNAME').head(3)
    ans = top_counties_df.groupby('STNAME').sum().sort_values(by = 'CENSUS2010POP', ascending = False).head(3).index.tolist()
    return ans

# print (answer_six())
# Reference: 
# https://github.com/Qian-Han/coursera-Applied-Data-Science-with-Python/blob/master/Introduction-to-Data-Science-in-Python/week2/week2_Assignment.ipynb
