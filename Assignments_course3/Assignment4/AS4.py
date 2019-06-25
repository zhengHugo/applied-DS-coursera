import pandas as pd
import numpy as np

df = pd.read_csv(
    '/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course3/Assignment4/train.csv', encoding='ISO 8859-1')
df.set_index = df['ticket_id']

# Only use these columns
columns = ['fine_amount', 'admin_fee', 'state_fee', 'late_fee', 'compliance']
df = df[columns]
df = df.dropna()

X_train = df[['fine_amount', 'admin_fee', 'state_fee', 'late_fee']]
print(X_train)
# y_train = df['compliance']
