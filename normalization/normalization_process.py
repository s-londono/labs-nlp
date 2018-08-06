import nltk
import re
import string
from pprint import pprint

LANG = "english"

corpus = [
    "The brown fox wasn't that quick and he couldn't win the race",
    "Hey that's a great deal! I just bought a phone for $199",
    "@@You'll (learn) a **lot** in the book. Python is an amazing language !@@"
]

# TEXT NORMALIZATION (a.k.a Text Wrangling or Cleansing)
# Process to wrangle, clean and standarize textual data into a form that can be analyzed and consumed by NLP systems-
# Consists of several steps:

# 1. CLEANING TEXT
# Remove extraneous and unnecessary tokens and characters. E.g. extract text from HTML, XML or JSON.
# Possible tools: NLTK's clean_html(), BeautifulSoup library to parse HTML, xpath, lxml library to parse XML.

# 1.1 Tokenize Text
# Depending on the problem/data, is usually performed before or after cleaning.
# The following is a function to tokenize a text corpus as a set of words.

def tokenize_text (text):

    sentences = nltk.sent_tokenize(text, language=LANG)

    words = [nltk.word_tokenize(sentence, language=LANG) for sentence in sentences]

    return words

pprint(tokenize_text(corpus[0]))
