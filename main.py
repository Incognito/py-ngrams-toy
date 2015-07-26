from textblob import TextBlob
from collections import Counter
import pprint

def main(text):
    tuples = get_tupels(text)
    counted = count_word_pairs(tuples)
    pprint.pprint(counted)

def get_tupels(text):
    lower = text.lower()
    blob = TextBlob(lower)
    ngrams = blob.ngrams(n=2)
    tuples = map(tuple,map(tuple, ngrams))
    return tuples

def count_word_pairs(tupleList):
    return Counter((frozenset(item)) for item in tupleList)
