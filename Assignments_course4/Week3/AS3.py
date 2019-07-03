from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import roc_auc_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
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


# What is the average length of documents (number of characters) for not spam and spam documents?
def answer_six():
    spams = spam_data[spam_data['target'] == 1]['text']
    not_spams = spam_data[spam_data['target'] == 0]['text']

    spam_len_list = [len(text) for text in spams]
    not_spam_len_list = [len(text) for text in not_spams]

    spam_len_avg = sum(spam_len_list)/len(spam_len_list)
    not_spam_len_avg = sum(not_spam_len_list)/len(not_spam_len_list)

    return (not_spam_len_avg, spam_len_avg)

# The following function has been provided to help you combine new features into the training data:


def add_feature(X, feature_to_add):
    """
    Returns sparse feature matrix with added feature.
    feature_to_add can also be a list of features.
    """
    from scipy.sparse import csr_matrix, hstack
    return hstack([X, csr_matrix(feature_to_add).T], 'csr')


# Fit and transform the training data X_train using a Tfidf Vectorizer ignoring terms that have a document frequency strictly lower than 5
# Using this document-term matrix and an additional feature, the length of document (number of characters), fit a Support Vector Classification model with regularization C=10000. Then compute the area under the curve (AUC) score using the transformed test data.
def answer_seven():
    vect = TfidfVectorizer(min_df=5).fit(X_train)
    X_train_vectorized = vect.fit_transform(X_train)
    X_test_vectorized = vect.transform(X_test)
    X_train_len = X_train.apply(len)
    X_test_len = X_test.apply(len)
    X_train_aug = add_feature(X_train_vectorized, X_train_len)
    X_test_aug = add_feature(X_test_vectorized, X_test_len)
    model = SVC(C=10000, gamma='auto')
    model.fit(X_train_aug, y_train)
    predictions = model.predict(X_test_aug)
    return roc_auc_score(y_test, predictions)
