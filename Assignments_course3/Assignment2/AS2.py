import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


np.random.seed(0)
n = 15
x = np.linspace(0, 10, n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10


X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)

# You can use this function to help you visualize the dataset by
# plotting a scatterplot of the data points
# in the training and test sets.


def part1_scatter():
    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(X_train, y_train, label='training data')
    plt.scatter(X_test, y_test, label='test data')
    plt.legend(loc=4)
    plt.show()


# NOTE: Uncomment the function below to visualize the data, but be sure
# to **re-comment it before submitting this assignment to the autograder**.
# part1_scatter()

'''
Write a function that fits a polynomial LinearRegression model on the training data X_train for degrees 1, 3, 6, and 9. (Use PolynomialFeatures in sklearn.preprocessing to create the polynomial features and then fit a linear regression model) For each model, find 100 predicted values over the interval x = 0 to 10 (e.g. np.linspace(0,10,100)) and store this in a numpy array. The first row of this array should correspond to the output from the model trained on degree 1, the second row degree 3, the third row degree 6, and the fourth row degree 9.
'''


def answer_one():
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures

    X_predict = np.linspace(0, 10, 100)  # column vector
    count = 0
    results = np.zeros([4, 100])
    for i in [1, 3, 6, 9]:
        poly = PolynomialFeatures(degree=i)
        X_train_poly = poly.fit_transform(X_train.reshape(-1, 1))
        X_predict_poly = poly.fit_transform(X_predict.reshape(-1, 1))
        linreg = LinearRegression().fit(X_train_poly, y_train)
        tmp_ans = linreg.predict(X_predict_poly)
        results[count, :] = tmp_ans
        count = count + 1
    return results

# feel free to use the function plot_one() to replicate the figure
# from the prompt once you have completed question one


def plot_one(degree_predictions):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    plt.plot(X_train, y_train, 'o', label='training data', markersize=10)
    plt.plot(X_test, y_test, 'o', label='test data', markersize=10)
    for i, degree in enumerate([1, 3, 6, 9]):
        plt.plot(np.linspace(0, 10, 100),
                 degree_predictions[i], alpha=0.8, lw=2, label='degree={}'.format(degree))
    plt.ylim(-1, 2.5)
    plt.legend(loc=4)
    plt.show()


'''
Write a function that fits a polynomial LinearRegression model on the training data X_train for degrees 0 through 9. For each model compute the  R2  (coefficient of determination) regression score on the training data as well as the the test data, and return both of these arrays in a tuple.

This function should return one tuple of numpy arrays (r2_train, r2_test). Both arrays should have shape (10,)
'''


def answer_two():
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.metrics.regression import r2_score
    results_train = np.zeros(10)
    results_test = np.zeros(10)
    for i in range(0, 10):
        poly = PolynomialFeatures(degree=i)
        X_train_poly = poly.fit_transform(X_train.reshape(-1, 1))
        X_test_poly = poly.fit_transform(X_test.reshape(-1, 1))
        linreg = LinearRegression().fit(X_train_poly, y_train)
        score_train = r2_score(y_train, linreg.predict(X_train_poly))
        score_test = r2_score(y_test, linreg.predict(X_test_poly))
        results_train[i] = score_train
        results_test[i] = score_test
    return (results_train, results_test)
