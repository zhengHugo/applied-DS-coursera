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


print(answer_one())
