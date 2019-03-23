import numpy as np
import pandas as pd


def answer_one():
    # ----------------------------------------------------------------------------------
    # Read energy
    energy = pd.read_excel('C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/Energy Indicators.xls',
                           skiprows=17, skipfooter=38)
    columns_keep = ['Unnamed: 1', 'Petajoules', 'Gigajoules', '%']
    energy = energy[columns_keep]
    columns = ['Country', 'Energy Supply',
               'Energy Supply per Capita', '% Renewable']
    energy.columns = columns
    energy.iloc[:, 1:4] = energy.iloc[:, 1:4].replace(
        '...', np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    energy['Country'] = energy['Country'].replace(
        {'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'China, Hong Kong Special Administrative Region': 'Hong Kong'})

    # Remove thing in () and revome abundant spaces
    energy['Country'] = energy['Country'].str.replace(
        r'\(.*\)', '', regex=True).str.strip()

    # ----------------------------------------------------------------------------------
    # Read GDP
    GDP = pd.read_csv(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/world_bank.csv', skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({
        'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'
    })
    # with pd.option_context('display.max_rows', None):
    # print(GDP['Country Name'])

    # Use last ten years of GDP data
    columns_to_keep = ['Country Name', '2006', '2007', '2008',
                       '2009', '2010', '2011', '2012', '2013', '2014', '2015', ]
    GDP = GDP[columns_to_keep]

    # ----------------------------------------------------------------------------------
    # Read ScimEn
    ScimEn = pd.read_excel(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/scimagojr-3.xlsx')

    # Use only the top 15 countries
    ScimEn = ScimEn[:15]

    # ----------------------------------------------------------------------------------
    # merge dataframes
    df = pd.merge(GDP, energy, how='inner',
                  left_on='Country Name', right_on='Country')
    df = pd.merge(df, ScimEn, how='inner',
                  left_on='Country Name', right_on='Country')
    df = df.set_index('Country Name')
    columns_to_keep = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index',
                       'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df = df[columns_to_keep]
    return df

# answer_one()


def answer_two():
    # Read energy
    energy = pd.read_excel('C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/Energy Indicators.xls',
                           skiprows=17, skipfooter=38)
    columns_keep = ['Unnamed: 1', 'Petajoules', 'Gigajoules', '%']
    energy = energy[columns_keep]
    columns = ['Country', 'Energy Supply',
               'Energy Supply per Capita', '% Renewable']
    energy.columns = columns
    energy.iloc[:, 1:4] = energy.iloc[:, 1:4].replace(
        '...', np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000
    energy['Country'] = energy['Country'].replace(
        {'Republic of Korea': 'South Korea', 'United States of America': 'United States', 'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom', 'China, Hong Kong Special Administrative Region': 'Hong Kong'})

    # Remove thing in () and revome abundant spaces
    energy['Country'] = energy['Country'].str.replace(
        r'\(.*\)', '', regex=True).str.strip()

    # ----------------------------------------------------------------------------------
    # Read GDP
    GDP = pd.read_csv(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/world_bank.csv', skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({
        'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'
    })
    # with pd.option_context('display.max_rows', None):
    # print(GDP['Country Name'])

    # Use last ten years of GDP data
    columns_to_keep = ['Country Name', '2006', '2007', '2008',
                       '2009', '2010', '2011', '2012', '2013', '2014', '2015', ]
    GDP = GDP[columns_to_keep]
    GDP.columns = ['Country', '2006', '2007', '2008',
                   '2009', '2010', '2011', '2012', '2013', '2014', '2015', ]

    # ----------------------------------------------------------------------------------
    # Read ScimEn
    ScimEn = pd.read_excel(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/scimagojr-3.xlsx')

    # ----------------------------------------------------------------------------------
    # merge dataframes
    df1 = pd.merge(GDP, energy, how='inner',
                   left_on='Country', right_on='Country')
    df1 = pd.merge(df1, ScimEn, how='inner',
                   left_on='Country', right_on='Country')
    df1 = df1.set_index('Country')
    df2 = pd.merge(GDP, energy, how='outer',
                   left_on='Country', right_on='Country')
    df2 = pd.merge(df2, ScimEn, how='outer',
                   left_on='Country', right_on='Country')
    df2 = df2.set_index('Country')
    columns_to_keep = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index',
                       'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df1 = df1[columns_to_keep]
    df2 = df2[columns_to_keep]
    return len(df2) - len(df1)


def answer_three():
    Top15 = answer_one()
    years = ['2006', '2007', '2008', '2009', '2010',
             '2011', '2012', '2013', '2014', '2015']
    Top15['Average'] = Top15[years].mean(axis=1)
    avgGDP = Top15['Average'].sort_values(ascending=False)
    return avgGDP


def answer_four():
    Top15 = answer_one()
    years = ['2006', '2007', '2008', '2009', '2010',
             '2011', '2012', '2013', '2014', '2015']
    Top15['Average'] = Top15[years].mean(axis=1)
    avgGDP = Top15['Average'].sort_values(ascending=False)
    idx = avgGDP.index[5]
    tgt_country = Top15.loc[idx]
    return tgt_country['2015'] - tgt_country['2006']


def answer_five():
    Top15 = answer_one()
    result = Top15['Energy Supply per Capita'].mean(axis=0)
    return result


def answer_six():
    Top15 = answer_one()
    target = Top15['% Renewable']
    max_idx = target.idxmax()
    return (max_idx, target.loc[max_idx])


def answer_seven():
    Top15 = answer_one()
    Top15['Ratio'] = Top15['Self-citations'] / Top15['Citations']
    target = Top15['Ratio']
    max_idx = target.idxmax()
    return (max_idx, target.loc[max_idx])


def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / \
        Top15['Energy Supply per Capita']
    Top15 = Top15.sort_values(by='Population', ascending=False)
    return Top15.iloc[2].name


def answer_nine():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / \
        Top15['Energy Supply per Capita']
    Top15['Citable Docs per Capita'] = Top15['Citable documents'] / \
        Top15['Population']
    ans = Top15['Citable Docs per Capita'].corr(
        Top15['Energy Supply per Capita'])
    return ans


def answer_ten():
    Top15 = answer_one()
    med = Top15['% Renewable'].median()
    Top15.sort_values(by='Rank')
    Top15['HighRenew'] = [1 if x >= med else 0 for x in Top15['% Renewable']]
    return Top15['HighRenew']


def answer_eleven():
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}
    Top15 = answer_one()
    Top15['PopEst'] = (Top15['Energy Supply'] /
                       Top15['Energy Supply per Capita'])
    Top15 = Top15.reset_index()
    Top15['Continent'] = [ContinentDict[country]
                          for country in Top15['Country Name']]
    target = Top15.set_index('Continent')
    target = target.groupby(target.index)[
        'PopEst'].agg([np.size, np.sum, np.mean, np.std])
    return target
