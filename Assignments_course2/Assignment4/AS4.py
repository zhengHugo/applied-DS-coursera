import pandas as pd
import matplotlib.pyplot as plt

basic_df = pd.read_csv(
    '/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course2/Assignment4/nflstatistics/Basic_Stats.csv')
# only focus on retired players
basic_df = basic_df[basic_df['Current Status'] == 'Retired']
basic_df = basic_df.drop(
    ['Age', 'High School', 'High School Location', 'Position', 'Number', 'Current Status', 'College', 'Current Team'], axis=1)
defend_df = pd.read_csv(
    '/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course2/Assignment4/nflstatistics/Career_Stats_Defensive.csv')
defend_df = defend_df[['Player Id',
                       'Team', 'Games Played', 'Total Tackles']]
df = defend_df.merge(basic_df, left_on='Player Id', right_on='Player Id')
df = df[['Player Id', 'Games Played', 'Total Tackles',
         'Height (inches)', 'Weight (lbs)']]
df = df[df['Total Tackles'].apply(lambda x: x.isdigit())]
df['Total Tackles'] = df['Total Tackles'].apply(lambda x: int(x))
df = df.groupby(['Player Id', 'Height (inches)', 'Weight (lbs)'], as_index=False)[
    'Games Played', 'Total Tackles'].apply(lambda x: x.sum()).reset_index()
df['Tackles per Game'] = df['Total Tackles']/df['Games Played']
df = df.rename(columns={'Height (inches)': 'Height', 'Weight (lbs)': 'Weight'})
columns = ['Height', 'Tackles per Game']
df_height = df[['Height', 'Tackles per Game']].copy()
df_weight = df[['Weight', 'Tackles per Game']].copy()
# print(df_height)
# print(df_weight)
fig, axes = plt.subplots(1, 2)
df_height['height_bin'] = pd.cut(df_height['Height'], bins=10)
df_height.boxplot(column='Tackles per Game', by='height_bin', ax=axes[0])
df_weight['weight_bin'] = pd.cut(df_weight['Weight'], bins=10)
df_weight.boxplot(column='Tackles per Game', by='weight_bin', ax=axes[1])

# print(df)
plt.show()
