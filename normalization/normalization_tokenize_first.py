import nltk
import re
import string
from pprint import pprint
from utils import CONTRACTION_MAP

LANG = "english"

raw_corpus = [
    "The brown fox wasn't that quick. Unfortunately, he couldn't win the race the dog won instead",
    "Hey that's a great deal! I just bought a phone for $199. You should check it out too, I'm sure you'll love it!",
    "@@You'll (learn) a **lot** in the book. Python is an amazing language !@@"
]

# TEXT NORMALIZATION (a.k.a Text Wrangling or Cleansing)
# Process to wrangle, clean and standarize textual data into a form that can be analyzed and consumed by NLP systems-
# Consists of several steps:


# 0. EXPAND CONTRACTIONS (MUST BE DONE BEFORE REMOVING APHOSTROPHES AT THE CLEANSING STEP)
# Avoid problems caused by contractions having aphostrophes (special character) and being ambiguous in some cases
# This implementation uses a map of contractions to their corresponding expansions, defined in utils.contractions
# IMPORTANT: note that some contractions can have multiple forms (e.g. you'll might be you will or you shall), the
# present implementation neglects those cases

def expand_contractions(sentence, contraction_mapping=CONTRACTION_MAP):

    # Create a regex pattern out of all the contractions in the contractions map
    contractions_pattern = re.compile("({})".format(
        "|".join(contraction_mapping.keys())), flags=re.IGNORECASE | re.DOTALL)

    def expand_match(contraction):

        match = contraction.group(0)
        first_char = match[0]

        exp_contraction = contraction_mapping.get(match, contraction_mapping.get(match.lower()))

        # Naive approach to preserving the case of the original word (first letter only)
        if first_char.lower() != exp_contraction[0].lower():
            exp_contraction = first_char + exp_contraction[1:]

        return exp_contraction

    return contractions_pattern.sub(expand_match, sentence)


corpus = [expand_contractions(sntnc) for sntnc in raw_corpus]

print("\nSTEP 0: EXPAND CONTRACTIONS: \n")
pprint([c for c in corpus])


# 1. TOKENIZE TEXT
# Depending on the problem/data, may performed before or after cleaning. Here text is tokenized before cleansing
# The following is a function to tokenize a text corpus as a set of words.

def tokenize_text(text):

    sentences = nltk.sent_tokenize(text, language=LANG)

    words = [nltk.word_tokenize(sentence, language=LANG) for sentence in sentences]

    return words


tokenized_corpus = [tokenize_text(c) for c in corpus]

print("\nSTEP 1: TOKENIZE CORPUS: \n")
pprint([sntnc for sntnc in tokenized_corpus])


# 2. REMOVE SPECIAL CHARACTERS
# Remove punctuation and special characters that are irrelevant for the analysis from the tokenized text

def remove_spec_chars_after_tokenization(tokens):

    pattern = re.compile("[{}]".format(re.escape(string.punctuation)))

    # Note how pattern.sub is used to remove all matches in each token.
    # The filter function filters out falsy items when its first argument is None, thus empty strings are removed
    filtered_tokens = filter(None, [pattern.sub("", token) for token in tokens])

    return [ft for ft in filtered_tokens]


# Note how filter is used to omit corpuses that end up being empty after cleaning up special characters
cleaned_corpus = []

for c in tokenized_corpus:
    cleaned_corpus.append(filter(None, [remove_spec_chars_after_tokenization(sntnc) for sntnc in c]))

cleaned_corpus = filter(None, cleaned_corpus)

# Reiterate to materialize the generators created by filter into actual lists
cleaned_corpus = [[sntnc for sntnc in cc] for cc in cleaned_corpus]

print("\nSTEP 2: CLEAN SPECIAL CHARACTERS OFF CORPUS AFTER TOKENIZATION: \n")
pprint([[sntnc for sntnc in cc] for cc in cleaned_corpus])


# 3. CASE CONVERSIONS
# Types of case conversions:
# - To lowercase/uppercase
# - Sentence case
# - Proper case

print("\nSTEP 4: CASE CONVERSIONS\n")
print([[tk.lower() for tk in sntnc] for sntnc in cleaned_corpus[0]])
print([[tk.upper() for tk in sntnc] for sntnc in cleaned_corpus[0]])


# 4. REMOVE STOP WORDS
# Words that have little or no significance. Are removed to retain words that are significant for anlyzing the text.
# Usually are the most frequent words such as: a, the, me, etc.
# Each domain and language has its own set of stopwords, there's no universal list.

def remove_stopwords(tokens):

    lst_stopwords = nltk.corpus.stopwords.words("english")

    return [tk for tk in tokens if tk not in lst_stopwords]


non_stop_corpus = filter(None, [[remove_stopwords(sntnc) for sntnc in c] for c in cleaned_corpus])

print("\nSTEP 4: REMOVE STOPWORDS\n")
pprint([nc for nc in non_stop_corpus])
