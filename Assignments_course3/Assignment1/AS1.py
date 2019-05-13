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
