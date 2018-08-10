import nltk
import re
import string
from pprint import pprint
from utils import CONTRACTION_MAP

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


def tokenize_text(text):

    sentences = nltk.sent_tokenize(text, language=LANG)

    words = [nltk.word_tokenize(sentence, language=LANG) for sentence in sentences]

    return words


print("\nSTEP 1: TOKENIZE CORPUS: \n")
pprint([tokenize_text(c) for c in corpus])

# 1.2 Remove Special Characters
# Can also be done before tokenizing text. Removes punctuation and special characters irrelevant for the analysis.

# - Variant 1: Remove special characters after tokenization:


def remove_spec_chars_after_tokenization(tokens):

    pattern = re.compile("[{}]".format(re.escape(string.punctuation)))

    # Note how pattern.sub is used to remove all matches in each token.
    # The filter function filters out falsy items when its first argument is None, thus empty strings are removed
    filtered_tokens = filter(None, [pattern.sub("", token) for token in tokens])

    return [ft for ft in filtered_tokens]


tokenized_corpus = [tokenize_text(c) for c in corpus]

# Note how filter is used to omit corpuses that end up being empty after cleaning up special characters
cleaned_corpus = filter(None, [remove_spec_chars_after_tokenization(tk) for tc in tokenized_corpus for tk in tc])

print("\nSTEP 2 (Variant 1): CLEAN SPECIAL CHARACTERS OFF CORPUS AFTER TOKENIZATION: \n")
pprint([cc for cc in cleaned_corpus])


# - Variant 2: Remove special characters before tokenization.
# This method provides the option to retain aphostropes, which sometimes are useful to expand them as contractions


def remove_spec_chars_before_tokenization(sentence, keep_aphostrophes=False):

    if keep_aphostrophes:
        # In this case, aphostrophes and periods will be retained
        pattern = re.compile(r"[?|$|&|*|%|@|(|)|~|{|}]")
    else:
        pattern = re.compile(r"\W")

    return pattern.sub("", sentence)


cleaned_corpus_ii = [remove_spec_chars_before_tokenization(c, True) for c in corpus]

print("\nSTEP 1 (Variant 2): CLEAN SPECIAL CHARACTERS OFF CORPUS BEFORE TOKENIZATION: \n")
pprint([cc for cc in cleaned_corpus_ii])

tokenized_corpus_ii = [tokenize_text(cc) for cc in cleaned_corpus_ii]

print("\nSTEP 2 (Variant 2): TOKENIZE PREVIOUSLY CLEANED UP CORPUS: \n")
pprint([cc for cc in tokenized_corpus_ii])


# 2. EXPAND CONTRACTIONS
# Avoid problems caused by contractions having aphostrophes (special character) and being ambiguous in some cases
# This implementation uses a map of contractions to their corresponding expansions, defined in utils.contractions
# IMPORTANT: note that some contractions can have multiple forms (e.g. you'll might be you will or you shall), the
# present implementation neglects those cases

def expand_contractions(sentence, contraction_mapping):




