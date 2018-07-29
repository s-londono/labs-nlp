import nltk
from nltk.corpus import gutenberg
from pprint import pprint

# Load the text to be tokenized
alice = gutenberg.raw(fileids="carroll-alice.txt")
print("- Alice corpus length:\t{}".format(len(alice)))
print("- Alice corpus sample:\t'{}'".format(alice[0:50]))

# Option 1: Create sentence tokenizer using the helper function sent_tokenize.
# This function tokenizes the sentences of the specified text using an instance of PunktSentenceTokenizer pre-trained
# in several language models to work reasonably well. The result is a list of strings (each being a sentence)
alice_sentences = nltk.sent_tokenize(alice, language="english")
pprint(alice_sentences[0:20])

