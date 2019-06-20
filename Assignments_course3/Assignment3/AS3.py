from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

df = pd.read_csv(
    '/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course3/Assignment3/fraud_data.csv')

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Use X_train, X_test, y_train, y_test for all the following questions

'''
Using X_train, X_test, y_train, and y_test (as defined above), train a dummy classifier that classifies everything as the majority class of the training data. What is the accuracy of this classifier? What is the recall?

This function should a return a tuple with two floats, i.e. (accuracy score, recall score).
'''


def answer_two():
    from sklearn.dummy import DummyClassifier
    from sklearn.metrics import recall_score, accuracy_score
    dummy_majority = DummyClassifier(
        strategy='most_frequent').fit(X_train, y_train)
    y_dummy = dummy_majority.predict(X_test)
    ans = (accuracy_score(y_test, y_dummy), recall_score(y_test, y_dummy))
    return ans


print(answer_two())
