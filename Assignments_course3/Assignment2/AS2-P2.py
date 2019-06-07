import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


mush_df = pd.read_csv(
    '/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course3/Assignment2/mushrooms.csv')
mush_df2 = pd.get_dummies(mush_df)
# mush_df: 8124 * 23
# mush_df2: 8124 * 119
X_mush = mush_df2.iloc[:, 2:]
y_mush = mush_df2.iloc[:, 1]

# use the variables X_train2, y_train2 for Question 5
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_mush, y_mush, random_state=0)

# For performance reasons in Questions 6 and 7, we will create a smaller version of the
# entire mushroom dataset for use in those questions.  For simplicity we'll just re-use
# the 25% test split created above as the representative subset.
#
# Use the variables X_subset, y_subset for Questions 6 and 7.
X_subset = X_test2
y_subset = y_test2

'''
Using X_train2 and y_train2 from the preceeding cell, train a DecisionTreeClassifier with default parameters and random_state=0. What are the 5 most important features found by the decision tree?

As a reminder, the feature names are available in the X_train2.columns property, and the order of the features in X_train2.columns matches the order of the feature importance values in the classifier's feature_importances_ property.

This function should return a list of length 5 containing the feature names in descending order of importance.

Note: remember that you also need to set random_state in the DecisionTreeClassifier.
'''


def answer_five():
    from sklearn.tree import DecisionTreeClassifier

    clf = DecisionTreeClassifier(random_state=0).fit(X_train2, y_train2)
    Series = pd.Series(data=clf.feature_importances_,
                       index=X_train2.columns.values)
    print(Series)

    results = Series.sort_values(axis=0, ascending=False).index.tolist()

    answer = results[:5]

    return answer


answer_five()
