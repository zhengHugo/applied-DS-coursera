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


print(question_one())
