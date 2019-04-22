import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv(
    'Assignments_course2/Assignment2/data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

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

# Get points when extrem temperature in 2015 exceed the last ten years
broke_min = minT_ave_15[minT_ave_15['Data_Value']
                        < minT_ave['Data_Value']].index.tolist()
broke_max = maxT_ave_15[maxT_ave_15['Data_Value']
                        > maxT_ave['Data_Value']].index.tolist()

plt.figure()
# Plot lines of temperature from 2005-2014
plt.plot(minT_ave['Data_Value'], 'b', label='High Temperatures')
plt.plot(maxT_ave['Data_Value'], 'r', label='Low Temperatures')
# Plot scatter points in 2015
plt.scatter(
    broke_min, minT_ave_15['Data_Value'].iloc[broke_min], s=20, c='k', alpha=0.5, label='Broken Min')
plt.scatter(
    broke_max, maxT_ave_15['Data_Value'].iloc[broke_max], s=20, c='g', alpha=0.5, label='Broken Max')
plt.xlabel('Month')
plt.ylabel('Temperature (Tenths of Degrees C)')
plt.title('Extreme Temperatures of 2015 against 2005-2014\n in Ann Arbor, Michigan, United States')
# Fill between the two lines with grey
plt.gca().fill_between(range(len(minT_ave)),
                       minT_ave['Data_Value'], maxT_ave['Data_Value'], facecolor='grey', alpha=0.3)
# Trim the axes
plt.gca().axis([-5, 370, -330, 350])
# Show legends and cut the frame
plt.legend(frameon=False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

a = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]
b = [i+15 for i in a]

Month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.xticks(b, Month_name)
plt.show()
