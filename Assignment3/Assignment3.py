import numpy as np
import pandas as pd


def answer_one():
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

    ScimEn = pd.read_excel(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment3/scimagojr-3.xlsx')

    # Use only the top 15 countries
    ScimEn = ScimEn[:15]
    df = pd.merge(GDP, energy, how='inner',
                  left_on='Country Name', right_on='Country')
    df = pd.merge(df, ScimEn, how='inner',
                  left_on='Country Name', right_on='Country')
    df = df.set_index('Country Name')
    columns_to_keep = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index',
                       'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    df = df[columns_to_keep]
    print(df)


answer_one()
