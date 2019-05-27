from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()


def answer_one():
    columns = cancer['feature_names'].tolist()
    df = pd.DataFrame(data=cancer['data'], columns=columns[:30])
    # pick the first 30 columns because only these features have data

    df['target'] = cancer['target']
    return df


def answer_two():
    cancerdf = answer_one()
    malignant_count = len(cancerdf[cancerdf['target'] == 0])
    benign_count = len(cancerdf[cancerdf['target'] == 1])
    index = ['malignant', 'benign']
    target = pd.Series(data=[malignant_count, benign_count], index=index)
    return target


def answer_three():
    cancerdf = answer_one()
    X = cancerdf.iloc[:, :30]
    y = cancerdf.iloc[:, 30]
    return (X, y)


def answer_four():
    X, y = answer_three()
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    return X_train, X_test, y_train, y_test


def answer_five():
    X_train, _, y_train, _ = answer_four()
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    return knn


def answer_six():
    cancerdf = answer_one()
    knn = answer_five()
    means = cancerdf.mean()[:-1].values.reshape(1, -1)
    prediction = knn.predict(means)
    ans = np.array(prediction)
    return ans


def answer_seven():
    _, X_test, _, _ = answer_four()
    knn = answer_five()
    prediction = knn.predict(X_test)
    return prediction


def answer_eight():
    _, X_test, _, y_test = answer_four()
    knn = answer_five()
    ans = knn.score(X_test, y_test)
    return ans
