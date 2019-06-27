import pandas as pd


doc = []
with open('/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course4/Week1/dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.DataFrame(doc)
df['id'] = df.index
df.columns = ['data', 'id']

# mm/dd/yyyy format
rg1 = r'(\d?\d)/(\d?\d)/(\d{2,4})'
df1 = df[df['data'].str.contains(rg1)]
df_remain = df.copy()
df_remain.drop(df1.index, inplace=True)
df1[['month', 'day', 'year']] = df1['data'].str.extract(
    rg1)

# mm-dd-yyyy format
rg2 = r'(\d?\d)-(\d?\d)-(\d{2,4})'
df2 = df_remain[df_remain['data'].str.contains(rg2)]
df_remain.drop(df2.index, inplace=True)
df2[['month', 'day', 'year']] = df2['data'].str.extract(
    rg2)

# dd MMM yyyy format
rg3 = r'(\d?\d) (Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) (\d{2,4})'
df3 = df_remain[df_remain['data'].str.contains(rg3)]
df3[['day', 'month', 'year']] = df3['data'].str.extract(rg3)
df3 = df3[['data', 'id', 'month', 'day', 'year']]  # rearrange column
df3['month'] = df3['month'].apply(lambda x: x[:3])
df_remain.drop(df3.index, inplace=True)

# Mmm+ dd, yyyy format
rg4 = r'(Jan(?:uary)?.?|Feb(?:ruary)?|Mar(?:ch)?.?|Apr(?:il)?.?|May.?|Jun(?:e)?.?|Jul(?:y)?.?|Aug(?:ust)?.?|Sep(?:tember)?.?|Oct(?:ober)?.?|Nov(?:ember)?.?|Dec(?:ember)?).? (\d?\d),? (\d{2,4})'
df4 = df_remain[df_remain['data'].str.contains(rg4)]
df4[['month', 'day', 'year']] = df4['data'].str.extract(rg4)
df4['month'] = df4['month'].apply(lambda x: x[:3])
df_remain.drop(df4.index, inplace=True)

# MMM+ yyyy format, day lost
rg5 = r'(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?).? (\d{2,4})'
df5 = df_remain[df_remain['data'].str.contains(rg5)]
df5[['month', 'year']] = df5['data'].str.extract(rg5)
df5['day'] = '1'
df5 = df5[['data', 'id', 'month', 'day', 'year']]
df5['month'] = df5['month'].apply(lambda x: x[:3])
df_remain.drop(df5.index, inplace=True)

# mm/yyyy, day lost
rg6 = r'(\d?\d)/(\d{2,4})'

df6 = df_remain[df_remain['data'].str.contains(rg6)]
df6[['month', 'year']] = df6['data'].str.extract(rg6)
df6['day'] = '1'
df6 = df6[['data', 'id', 'month', 'day', 'year']]
df_remain.drop(df6.index, inplace=True)

# Typo entries
df8 = df_remain.loc[[298, 313]]
df8['month'] = ['1', '12']
df8['day'] = '1'
df8['year'] = ['1993', '1978']
df_remain.drop(df8.index, inplace=True)
df_remain.to_csv(path_or_buf='~/Downloads/abc.csv')

# yyyy, year only
rg7 = r'(\d\d\d\d)'
df7 = df_remain[df_remain['data'].str.contains(rg7)]
df7['year'] = df7['data'].str.extract(rg7)
df7['month'] = '1'
df7['day'] = '1'
df7 = df7[['data', 'id', 'month', 'day', 'year']]
df_remain.drop(df7.index, inplace=True)

# Process df3, df4, df5
months = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6',
          'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
df3['month'] = df3['month'].apply(lambda x: months[x])
df4['month'] = df4['month'].apply(lambda x: months[x])
df5['month'] = df5['month'].apply(lambda x: months[x])

dfx = df1.append(df2).append(df3).append(df4).append(
    df5).append(df6).append(df7).append(df8)


def processYear(year):
    year = int(year)
    if 50 <= year < 1000:
        year += 1900
    return year


dfx['year'] = dfx['year'].apply(processYear)
dfx['month'] = dfx['month'].apply(int)
dfx['day'] = dfx['day'].apply(int)
dfx = dfx.sort_values(by=['year', 'month', 'day'])
ans = pd.Series(dfx['id']).reset_index(drop=True)
