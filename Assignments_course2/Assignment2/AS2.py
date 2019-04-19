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

# trim
df = df[(df['Month-Day'] != '02-29')]

# Separate the data by min temperature and max temperature
df_minT = df[(df['Element'] == 'TMIN')]
df_maxT = df[(df['Element'] == 'TMAX')]

# Get 2015 data
df_minT_15 = df_minT[(df_minT['Year'] == '2015')]
df_maxT_15 = df_maxT[(df_maxT['Year'] == '2015')]
# Cut out the year 2015 since we only need 2005-2014
df_minT = df_minT[(df_minT['Year'] != '2015')]
df_maxT = df_maxT[(df_maxT['Year'] != '2015')]

# Get the area temperature by averaging data from each station
minT_ave = df_minT.groupby('Month-Day')['Data_Value'].agg(np.mean)
maxT_ave = df_maxT.groupby('Month-Day')['Data_Value'].agg(np.mean)
minT_ave_15 = df_minT_15.groupby('Month-Day')['Data_Value'].agg(np.mean)
maxT_ave_15 = df_maxT_15.groupby('Month-Day')['Data_Value'].agg(np.mean)

# Reset the index from Month-Day for the convenience of labling the
# x-axis in the plot
minT_ave = minT_ave.reset_index()
maxT_ave = maxT_ave.reset_index()
minT_ave_15 = minT_ave_15.reset_index()
maxT_ave_15 = maxT_ave_15.reset_index()

broke_min = minT_ave_15[minT_ave_15['Data_Value']
                        < minT_ave['Data_Value']].index.tolist()
broke_max = maxT_ave_15[maxT_ave_15['Data_Value']
                        < maxT_ave['Data_Value']].index.tolist()
print(broke_max)
print(broke_min)


# plt.figure()
# plt.plot(minT_ave['Data_Value'], 'b', alpha=0.5, label='High Temperatures')
# plt.plot(maxT_ave['Data_Value'], 'r', alpha=0.5, label='Low Temperatures')
# plt.show()
