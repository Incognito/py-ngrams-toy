from textblob import TextBlob
import pprint

def main(text):
    tuples = get_tupels(lower)
    pprint.pprint(tuples)

def get_tupels(text):
    lower = text.lower()
    blob = TextBlob(text)
    return map(tuple, blob.ngrams(n=2))

def count_word_pairs():
    return []
