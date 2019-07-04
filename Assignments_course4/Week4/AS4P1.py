import numpy as np
import nltk
from nltk.corpus import wordnet as wn
import pandas as pd


def convert_tag(tag):
    """Convert the tag given by nltk.pos_tag to the tag used by wordnet.synsets"""

    tag_dict = {'N': 'n', 'J': 'a', 'R': 'r', 'V': 'v'}
    try:
        return tag_dict[tag[0]]
    except KeyError:
        return None


def doc_to_synsets(doc):
    """
    Returns a list of synsets in document.

    Tokenizes and tags the words in the document doc.
    Then finds the first synset for each word/tag combination.
    If a synset is not found for that combination it is skipped.

    Args:
        doc: string to be converted

    Returns:
        list of synsets

    Example:
        doc_to_synsets('Fish are nvqjp friends.')
        Out: [Synset('fish.n.01'), Synset('be.v.01'), Synset('friend.n.01')]
    """

    token = nltk.word_tokenize(doc)
    tag = nltk.pos_tag(token)
    nltk2wordnet = [(i[0], convert_tag(i[1])) for i in tag]
    # if there are no synsets in token, ignore, else put in a list
    output = [wn.synsets(i, z)[0]
              for i, z in nltk2wordnet if len(wn.synsets(i, z)) > 0]

    return output


def similarity_score(s1, s2):
    """
    Calculate the normalized similarity score of s1 onto s2

    For each synset in s1, finds the synset in s2 with the largest similarity value.
    Sum of all of the largest similarity values and normalize this value by dividing it by the number of largest similarity values found.

    Args:
        s1, s2: list of synsets from doc_to_synsets

    Returns:
        normalized similarity score of s1 onto s2

    Example:
        synsets1 = doc_to_synsets('I like cats')
        synsets2 = doc_to_synsets('I like dogs')
        similarity_score(synsets1, synsets2)
        Out: 0.73333333333333339
    """

    list1 = []
    for s in s1:
        list1.append(max([i.path_similarity(s)
                          for i in s2 if i.path_similarity(s) is not None]))

    output = sum(list1)/len(list1)

    return output


def document_path_similarity(doc1, doc2):
    """Finds the symmetrical similarity between doc1 and doc2"""

    synsets1 = doc_to_synsets(doc1)
    synsets2 = doc_to_synsets(doc2)

    return (similarity_score(synsets1, synsets2) + similarity_score(synsets2, synsets1)) / 2


paraphrases = pd.read_csv('Assignments_course4/Week4/paraphrases.csv')


def most_similar_docs():

    def func(x):
        try:
            return document_path_similarity(x['D1'], x['D2'])
        except:
            return np.nan

    paraphrases['similarity_score'] = paraphrases.apply(func, axis=1)
    df = paraphrases.sort_values('similarity_score', ascending=False)

    return (df['D1'].iloc[0], df['D2'].iloc[0], df['similarity_score'].iloc[0])


def label_accuracy():
    from sklearn.metrics import accuracy_score

    def func(x):
        try:
            return document_path_similarity(x['D1'], x['D2'])
        except:
            return np.nan

    paraphrases['similarity_score'] = paraphrases.apply(func, axis=1)
    df = paraphrases.copy()
    # drop the nan line in dataframe
    df = df.dropna()

    # assign labels to the dataframe
    df['label'] = df['similarity_score'].apply(
        lambda x: 1 if x > 0.75 else 0)

    output = accuracy_score(df['Quality'], df['label'])

    return output


print(label_accuracy())
