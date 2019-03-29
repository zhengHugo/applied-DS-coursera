import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina',
          'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


def get_list_of_university_towns():
    '''
        Returns a DataFrame of towns and the states they are in from the
        university_towns.txt list. The format of the DataFrame should be:
        DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
        columns=["State", "RegionName"]  )

        The following cleaning needs to be done:

        1. For "State", removing characters from "[" to the end.
        2. For "RegionName", when applicable, removing every character from " (" to the end.
        3. Depending on how you read the data, you may need to remove newline character '\n'.
    '''

    with open('C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment4/university_towns.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    state_town = []
    for line in content:
        if '[edit]' in line:
            state = line[:-6]
        elif '(' in line:
            town = line.split('(')[0].strip()
            state_town.append([state, town])
        elif ',' in line:
            # two lines are in a improper format, add manually
            town = line.split(',')[0].strip()
            state_town.append([state, town])
    ans = pd.DataFrame(state_town, columns=['State', 'RegionName'])
    return ans


def get_recession_start():
    '''
        Returns the year and quarter of the recession start time as a string value in a format such as 2005q3
    '''
    df = pd.read_excel(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment4/gdplev.xls', skiprows=7)
    df = df[['Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Quarters', 'GDP']
    df = df.iloc[212:]
    recessions_start = []
    for i in range(len(df) - 2):
        if df.iloc[i][1] > df.iloc[i+1][1] and df.iloc[i+1][1] > df.iloc[i+2][1]:
            recessions_start.append(df.iloc[i][0])
    return recessions_start[0]


def get_recession_end():
    '''
        Returns the year and quarter of the recession end time as a
        string value in a format such as 2005q3
    '''
    df = pd.read_excel(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment4/gdplev.xls', skiprows=7)
    df = df[['Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Quarters', 'GDP']
    df = df.iloc[212:]
    recessions_end = []
    for i in range(len(df) - 3):
        if df.iloc[i][1] > df.iloc[i+1][1] > df.iloc[i+2][1] and df.iloc[i+2][1] < df.iloc[i+3][1] < df.iloc[i+4][1]:
            recessions_end.append(df.iloc[i+4][0])
    return recessions_end[0]


def get_recession_bottom():
    '''
        Returns the year and quarter of the recession bottom time as a 
        string value in a format such as 2005q3
    '''

    df = pd.read_excel(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment4/gdplev.xls', skiprows=7)
    df = df[['Unnamed: 4', 'Unnamed: 5']]
    df.columns = ['Quarters', 'GDP']
    df = df.iloc[212:]
    recessions_bottom = []
    for i in range(len(df) - 3):
        if df.iloc[i][1] > df.iloc[i+1][1] > df.iloc[i+2][1] and df.iloc[i+2][1] < df.iloc[i+3][1] < df.iloc[i+4][1]:
            recessions_bottom.append(df.iloc[i+2][0])
    return recessions_bottom[0]


def convert_housing_data_to_quarters():
    '''
        Converts the housing data to quarters and returns it as mean values in a dataframe. 
        This dataframe should be a dataframe with columns for 2000q1 through 2016q3, and should have a multi-index in the shape of ["State","RegionName"].
        Note: Quarters are defined in the assignment description, they are not arbitrary three month periods.
        The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    df = pd.read_csv(
        'C:/Users/11796/Documents/Study_Materials/Applied_Data_Science/Assignments/Assignment4/City_Zhvi_AllHomes.csv')
    df = df.drop(df.columns[[0] + list(range(3, 51))], axis=1)
    for year in range(2000, 2016):
        spring_column = [str(year) + '-01', str(year) +
                         '-02', str(year) + '-03']
        summer_column = [str(year) + '-04', str(year) +
                         '-05', str(year) + '-06']
        fall_column = [str(year) + '-07', str(year) + '-08', str(year) + '-09']
        winter_column = [str(year) + '-10', str(year) +
                         '-11', str(year) + '-12']
        df[str(year) + 'q1'] = df[spring_column].mean(axis=1)
        df[str(year) + 'q2'] = df[summer_column].mean(axis=1)
        df[str(year) + 'q3'] = df[fall_column].mean(axis=1)
        df[str(year) + 'q4'] = df[winter_column].mean(axis=1)
    year = 2016
    spring_column = [str(year) + '-01', str(year) +
                     '-02', str(year) + '-03']
    summer_column = [str(year) + '-04', str(year) +
                     '-05', str(year) + '-06']
    fall_column = [str(year) + '-07', str(year) + '-08', str(year) + '-09']
    df[str(year) + 'q1'] = df[spring_column].mean(axis=1)
    df[str(year) + 'q2'] = df[summer_column].mean(axis=1)
    df[str(year) + 'q3'] = df[[str(year) + '-07', str(year) + '-08']].mean(axis=1)

    df = df.drop(df.columns[2:202], axis=1)
    df['State'] = [states[state] for state in df['State']]
    df = df.set_index(['State', 'RegionName'])
    return df


print(convert_housing_data_to_quarters())
