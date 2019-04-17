import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv(
    'C:\\Users\\11796\\Documents\\Study_Materials\\Coursera\\Applied_Data_Science\\Assignments\\Assignments_course2\\Assignment2\\data\\C2A2_data\\BinnedCsvs_d400\\fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

df = df.sort_values('Date', ascending=True)

# Process the date
df['Year'] = df['Date'].str[:4]
df['Month'] = df['Date'].str[5:7]
df['Day'] = df['Date'].str[8:10]
df['Month-Day'] = df['Date'].str[5:10]

# Separate the data by min temperature and max temperature
df_minT = df[(df['Element'] == 'TMIN')]
df_maxT = df[(df['Element'] == 'TMAX')]
# Cut out the year 2015 since we only need 2005-2014
df_minT = df_minT[(df_minT['Year'] != '2015')]
df_maxT = df_maxT[(df_maxT['Year'] != '2015')]


minT_ave = df_minT.groupby(
    'Month-Day')['Data_Value'].agg(np.mean)
maxT_ave = df_maxT.groupby(
    'Month-Day')['Data_Value'].agg(np.mean)


print(type(minT_ave))
print(type(maxT_ave))
print(minT_ave['value'])
# plt.figure()
# plt.plot(minT_ave, 'y')
# plt.show()
