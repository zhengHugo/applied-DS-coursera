from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

spam_data = pd.read_csv('Assignments_course4/Week3/spam.csv')
spam_data['target'] = np.where(spam_data['target'] == 'spam', 1, 0)
X_train, X_test, y_train, y_test = train_test_split(
    spam_data['text'], spam_data['target'], random_state=0)


# What percentage of the documents in spam_data are spam?
def answer_one():
    ans = len(spam_data[spam_data['target'] == 1]) / len(spam_data) * 100
    return ans


# Fit the training data X_train using a Count Vectorizer with default parameters.
# What is the longest token in the vocabulary?
def answer_two():
    data = spam_data['text']
    vect = CountVectorizer().fit(data)
    sortedWords = sorted(vect.get_feature_names(), key=len)
    return sortedWords[-1]


# Fit and transform the training data X_train using a Count Vectorizer with default parameters.
# Next, fit a fit a multinomial Naive Bayes classifier model with smoothing alpha=0.1. Find the area under the curve (AUC) score using the transformed test data.
def answer_three():
    vect = CountVectorizer().fit(X_train)
    X_train_vectorized = vect.transform(X_train)
    model = MultinomialNB(alpha=0.1)
    model.fit(X_train_vectorized, y_train)
    predictions = model.predict(vect.transform(X_test))
    return roc_auc_score(y_test, predictions)


# Fit and transform the training data X_train using a Tfidf Vectorizer with default parameters.
# What 20 features have the smallest tf-idf and what 20 have the largest tf-idf?
def answer_four():
    vect = TfidfVectorizer().fit(X_train)
    X_train_vectorized = vect.transform(X_train)
    values = X_train_vectorized.max(0).toarray()[0]
    index = vect.get_feature_names()
    features_series = pd.Series(values, index=index)
    return (features_series.nsmallest(20), features_series.nlargest(20))


# Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document frequency strictly lower than 3.
def answer_five():
    vect = TfidfVectorizer(min_df=3).fit(X_train)
    X_train_vectorized = vect.transform(X_train)
    model = MultinomialNB(alpha=0.1)
    model.fit(X_train_vectorized, y_train)
    predictions = model.predict(vect.transform(X_test))
    return roc_auc_score(y_test, predictions)
