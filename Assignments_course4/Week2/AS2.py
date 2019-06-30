from nltk.stem import WordNetLemmatizer
import nltk
import pandas as pd
import numpy as np

# If you would like to work with the raw text you can use 'moby_raw'
with open('/Users/hugozheng/Documents/StudyMaterials/Coursera/Applied_Data_Science/Assignments/Assignments_course4/Week2/moby.txt', 'r') as f:
    moby_raw = f.read()

# If you would like to work with the novel in nltk.Text format you can use 'text1'
moby_tokens = nltk.word_tokenize(moby_raw)
text1 = nltk.Text(moby_tokens)


# How many tokens (words and punctuation symbols) are in text1?
def example_one():
    return len(nltk.word_tokenize(moby_raw))


# How many unique tokens (unique words and punctuation) does text1 have?
def example_two():
    return len(set(nltk.word_tokenize(moby_raw)))


# After lemmatizing the verbs, how many unique tokens does text1 have?
def example_three():
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(w, 'v') for w in text1]
    return len(set(lemmatized))


# What is the lexical diversity of the given text input? (i.e. ratio of unique tokens to the total number of tokens)
def question_one():
    return example_two()/example_one()

# What percentage of tokens is 'whale'or 'Whale'?


def question_two():
    wdist = nltk.FreqDist(moby_tokens)
    count = wdist['whale'] + wdist['Whale']
    return 100 * count / example_one()


# What are the 20 most frequently occurring (unique) tokens in the text? What is their frequency?
def question_three():
    fdist = nltk.FreqDist(moby_tokens)
    return fdist.most_common(20)


# What tokens have a length of greater than 5 and frequency of more than 150?
def question_four():
    fdist = nltk.FreqDist(moby_tokens)
    df = pd.DataFrame(fdist.most_common(), columns=["token", "frequency"])
    freqwords = df[(df.token.str.len() > 5) & (df.frequency > 150)]
    return sorted(freqwords.token)


# Find the longest word in text1 and that word's length.
def question_five():
    fdist = nltk.FreqDist(text1)
    df = pd.DataFrame(fdist.most_common(), columns=["token", "frequency"])
    tokenList = df['token']
    target = sorted(tokenList, key=len, reverse=True)
    return (target[0], len(target[0]))


# What unique words have a frequency of more than 2000? What is their frequency?
def question_six():
    fdist = nltk.FreqDist(moby_tokens)
    df = pd.DataFrame(fdist.most_common(), columns=["token", "frequency"])
    freqwords = df[(df.token.str.isalpha()) & (df.frequency > 2000)]

    # the following steps convert dataframe into a set of tuples

    subset = freqwords[['frequency', 'token']]
    tuples = [tuple(x) for x in subset.values]
    return tuples


print(question_six())
