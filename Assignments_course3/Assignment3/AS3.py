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


'''
Using X_train, X_test, y_train, y_test (as defined above), train a SVC classifer using the default parameters. What is the accuracy, recall, and precision of this classifier?

This function should a return a tuple with three floats, i.e. (accuracy score, recall score, precision score).
'''


def answer_three():
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, recall_score, precision_score

    svm = SVC(gamma='auto').fit(X_train, y_train)
    y_predict = svm.predict(X_test)
    acc_score = accuracy_score(y_test, y_predict)
    rec_score = recall_score(y_test, y_predict)
    pre_score = precision_score(y_test, y_predict)
    return(acc_score, rec_score, pre_score)


'''
Using the SVC classifier with parameters {'C': 1e9, 'gamma': 1e-07}, what is the confusion matrix when using a threshold of -220 on the decision function. Use X_test and y_test.

This function should return a confusion matrix, a 2x2 numpy array with 4 integers.
'''


def answer_four():
    from sklearn.svm import SVC
    from sklearn.metrics import confusion_matrix

    svm = SVC(C=1e9, gamma=1e-07).fit(X_train, y_train)
    y_predict = svm.decision_function(X_test) > -220
    confusion = confusion_matrix(y_test, y_predict)
    return confusion
