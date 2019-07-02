from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

spam_data = pd.read_csv('Assignments_course4/Week3/spam.csv')
spam_data['target'] = np.where(spam_data['target'] == 'spam', 1, 0)
x_train, X_test, y_train, y_test = train_test_split(
    spam_data['text'], spam_data['target'], random_state=0)


# What percentage of the documents in spam_data are spam?
def answer_one():
    ans = len(spam_data[spam_data['target'] == 1]) / len(spam_data) * 100
    return ans


# Fit the training data X_train using a Count Vectorizer with default parameters.
# What is the longest token in the vocabulary?


def answer_two():
    X_train = spam_data['text']
    vect = CountVectorizer().fit(X_train)
    sortedWords = sorted(vect.get_feature_names(), key=len)
    return sortedWords[-1]


print(answer_two())
