import pandas as pd

census_df = pd.read_csv(
    'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment2/census.csv')
# print(census_df.head())
# print(census_df.loc[:,['SUMLEV', 'STATE', 'COUNTY']])

'''
    Which state has the most counties in it? (hint: consider the sumlevel key
    carefully! You'll need this for future questions too...)
    This function should return a single string value
'''


def answer_five():
    states = census_df['STNAME'].unique()
    county_num = pd.Series([0] * len(states), index=states)
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
    top_counties_df = counties_df.sort_values(
        by='CENSUS2010POP', ascending=False).groupby('STNAME').head(3)
    ans = top_counties_df.groupby('STNAME').sum().sort_values(
        by='CENSUS2010POP', ascending=False).head(3).index.tolist()
    return ans

# print (answer_six())
# Reference:
# https://github.com/Qian-Han/coursera-Applied-Data-Science-with-Python/blob/master/Introduction-to-Data-Science-in-Python/week2/week2_Assignment.ipynb


'''
    Which county has had the largest absolute change in population within the period 2010-2015? 
    (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, 
    you need to consider all six columns)
    
    e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest
    change in the period would be |130-80| = 50

    This function should return a single string value
'''


def answer_seven():
    counties_df = census_df[census_df['SUMLEV'] == 50]
    counties_df = counties_df.set_index('CTYNAME')
    columns = [
        'POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015'
    ]
    max_value = counties_df[columns].max(axis=1)
    min_value = counties_df[columns].min(axis=1)
    diff = max_value - min_value
    counties_df['diff'] = diff
    ans = counties_df['diff'].idxmax()
    return ans

# print(answer_seven())


'''
    In this datafile, the United States is broken up into four regions using the "REGION" column.

    Create a query that finds the countries that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE 2015 was greater thn their POPESTIMATE 2014.
    
    This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
'''


def answer_eight():
    counties_df = census_df[census_df['SUMLEV'] == 50]
    ans = counties_df[((counties_df['REGION'] == 1) | (counties_df['REGION'] == 2)) & (counties_df['CTYNAME'].str.slice(stop=10) == 'Washington') & (
        counties_df['POPESTIMATE2015'] > counties_df['POPESTIMATE2014'])][['STNAME', 'CTYNAME']]
    return ans


print(answer_eight())
