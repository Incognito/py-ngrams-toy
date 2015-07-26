from textblob import TextBlob
from collections import Counter
import sys

def main(text):
    tuples = get_tupels(text)
    counted = count_word_pairs(tuples)
    filtered = [item for item in counted.most_common() if item[1] > 1]
    result = display(filtered)
    return result

def get_tupels(text):
    lower = text.lower()
    blob = TextBlob(lower)
    ngrams = blob.ngrams(n=2) # assumption: don't is two words (do n't), as in "do not"
                              # this can be easily changed by modifying the tokenizer
                              # http://stackoverflow.com/questions/30550411
    tuples = map(tuple,map(tuple, ngrams))
    return tuples

def count_word_pairs(tupleList):
    return Counter((frozenset(item)) for item in tupleList)

def display(results):
    output = ""
    for result in results:
        words = list(result[0])
        output = output + "\n" + (words[0] + " " + words[1] + ": " + str(result[1]))

    return output

if __name__ == "__main__":
    for line in sys.stdin:
        print(main(line))
