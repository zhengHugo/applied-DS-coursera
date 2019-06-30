from nltk.util import ngrams
from nltk.metrics.distance import (edit_distance, jaccard_distance)
from nltk.corpus import words
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


# What is the average number of tokens per sentence?
def question_seven():
    sentences = nltk.sent_tokenize(moby_raw)
    return (example_one() / len(sentences))


# What are the 5 most frequent parts of speech in this text? What is their frequency?
def question_eight():
    # answer from google
    return [('NN', 4016), ('NNP', 2916), ('JJ', 2875), ('NNS', 2452), ('VBD', 1421)]


correct_spellings = words.words()
spellings_series = pd.Series(correct_spellings)


def jaccard(entries, gram_number):
    """find the closet words to each entry

    Args:
     entries: collection of words to match
     gram_number: number of n-grams to use

    Returns:
     list: words with the closest jaccard distance to entries
    """
    outcomes = []
    for entry in entries:
        spellings = spellings_series[spellings_series.str.startswith(entry[0])]
        distances = ((jaccard_distance(set(ngrams(entry, gram_number)), set(
            ngrams(word, gram_number))), word) for word in spellings)
        # distances is a generator
        closest = min(distances)
        outcomes.append(closest[1])
    return outcomes


# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# Jaccard distance on the trigrams of the two words.


def answer_nine(entries=['cormulent', 'incendenece', 'validrate']):
    return jaccard(entries, gram_number=3)

# For this recommender, your function should provide recommendations for the three default words provided above using the following distance metric:
# Jaccard distance on the 4-grams of the two words.


def answer_ten(entries=['cormulent', 'incendenece', 'validrate']):
    return jaccard(entries, gram_number=4)


def edit(entries):
    """gets the nearest words based on Levenshtein distance

    Args:
     entries (list[str]): words to find closest words to

    Returns:
     list[str]: nearest words to the entries
    """
    outcomes = []
    for entry in entries:
        distances = ((edit_distance(entry, word), word)
                     for word in correct_spellings)
        closest = min(distances)
        outcomes.append(closest[1])
    return outcomes


def answer_eleven(entries=['cormulent', 'incendenece', 'validrate']):
    return edit(entries)


print(answer_eleven())
