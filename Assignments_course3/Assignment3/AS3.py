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
    svm_predict = svm.decision_function(X_test) > -220
    confusion = confusion_matrix(y_test, svm_predict)
    return confusion


'''
Train a logisitic regression classifier with default parameters using X_train and y_train.
For the logisitic regression classifier, create a precision recall curve and a roc curve using y_test and the probability estimates for X_test (probability it is fraud).
Looking at the precision recall curve, what is the recall when the precision is 0.75?
Looking at the roc curve, what is the true positive rate when the false positive rate is 0.16?
This function should return a tuple with two floats, i.e. (recall, true positive rate).
'''


def answer_five():
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import precision_recall_curve, roc_curve
    import matplotlib.pyplot as plt
    lr = LogisticRegression(solver='liblinear').fit(X_train, y_train)
    lr_scores = lr.decision_function(X_test)
    precision, recall, _ = precision_recall_curve(y_test, lr_scores)
    closest_zero_p = np.argmin(np.abs(precision-0.75))
    closest_zero_r = recall[closest_zero_p]
    fpr_lr, tpr_lr, _ = roc_curve(y_test, lr_scores)
    closest_zero_fpr_lr = np.argmin(np.abs(fpr_lr - 0.16))
    closest_zero_tpr_lr = tpr_lr[closest_zero_fpr_lr]
    return (closest_zero_r, closest_zero_tpr_lr)


'''
Perform a grid search over the parameters listed below for a Logisitic Regression classifier, using recall for scoring and the default 3-fold cross validation.

'penalty': ['l1', 'l2']

'C':[0.01, 0.1, 1, 10, 100]

From .cv_results_, create an array of the mean test scores of each parameter combination. i.e.
'''


def answer_six():
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import GridSearchCV
    lr = LogisticRegression(solver='liblinear')
    param = {'C': [0.01, 0.1, 1, 10, 100], 'penalty': ['l1', 'l2']}
    grid_lr = GridSearchCV(lr, param_grid=param,
                           scoring='recall', cv=3).fit(X_train, y_train)
    return grid_lr.cv_results_['mean_test_score'].reshape(5, 2)
