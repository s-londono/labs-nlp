import nltk
from nltk.corpus import gutenberg
from nltk.corpus import europarl_raw
from pprint import pprint

# Load the text to be tokenized
alice = gutenberg.raw(fileids="carroll-alice.txt")
print("- Alice corpus length:\t{}".format(len(alice)))
print("- Alice corpus sample:\t'{}'".format(alice[0:50]))

# Option 1: Sentence tokenize using the helper function sent_tokenize.
# This function tokenizes the sentences of the specified text using an instance of PunktSentenceTokenizer pre-trained
# in several language models to work reasonably well. The result is a list of strings (each being a sentence)
print("\n\n-- EXAMPLE 1: ALICE IN WONDERLAND. DEFAULT SENT_TOKENIZE FUNCTION\n")

alice_sentences = nltk.sent_tokenize(alice, language="english")

print("\nTotal sentences in Alice: {}".format(len(alice_sentences)))
print("Sample sentences from Alice: ")
pprint(alice_sentences[0:20])

# Note how the sent_tokenize function can be used to tokenize text in other languages, as it uses a tokenized that is
# pre-trained in several laguages!
print("\n\n-- EXAMPLE 2: TEXT IN GERMAN. DEFAULT SENT_TOKENIZE FUNCTION\n")

german_text = europarl_raw.german.raw(fileids='ep-00-01-17.de')
print("Euro Parlament German text. Total length: {}".format(len(german_text)))
pprint(german_text[2:150], width=80)

german_sentences = nltk.sent_tokenize(german_text, language="german")

print("\nTotal sentences in Euro Parlament German: {}".format(len(german_sentences)))
print("Sample sentences from Euro Parlament German: ")
pprint(german_sentences[0:20])








