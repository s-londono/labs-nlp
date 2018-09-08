import re
from pprint import pprint
import nltk
import collections

# Based on Peter Norvig's: http://norvig.com/spell-correct.html

# Objective: given a word, find the most likely word that is the correct form of that word
#
# 1. Generate a set of candidate words that are near to the input word
# 2. Select the most likely word from the set as the correct word
#
# Uset the edit distance: how far or near is a word from the input word


def tokens(text):
    """
    Get all words that are made up of lowercase characters, from the corpus
    :param text: text of the corpus
    :return: array of lowercase words
    """
    return re.findall(r"[a-z]+", text.lower())


# Build a map (dictionary) of words in the corpus, with the total number of times each word appears as value
WORDS = None

with open("../datasets/big.txt", encoding="ascii") as file:

    WORDS = tokens(file.read())

WORD_COUNTS = collections.Counter(WORDS)

# Top 10 words in the corpus
print(WORD_COUNTS.most_common(10))

# 3. Define functions to find the words that are 0, 1 and 2 edits away from a specific word.
# Here edits refer to either insertions, deletions and transpositions


def edits0(word):
    """Returns all strings that are zero edits away from word"""

    return {word}


def edits1(word):
    """Returns all strings that are one edit away from word"""

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def splits(word_to_split):
        """Return a list of all possible (first, rest) pairs that the input word is made of"""

        return [(word_to_split[:i], word_to_split[i:]) for i in range(len(word_to_split) + 1)]

    pairs = splits(word)

    deletes = [a + b[1:] for (a, b) in pairs if b]

    transposes = [a + b[1] + b[0] + b[2:] for (a, b) in pairs if len(b) > 1]

    replaces = [a + c + b[1:] for (a, b) in pairs if b for c in alphabet]

    inserts = [a + c + b for (a, b) in pairs for c in alphabet]

    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """Returns all strings that are two edits away from word"""

    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}


def known(words):
    """Returns a subset of the provided set of words, which contains all members that are actually in the
       dictionary of known words (WORD_COUNTS)
    """

    return {w for w in words if w in WORD_COUNTS}


# Define the definitive function to correct a word

def correct(word):
    """Get the best candidate correct spelling for the input word
       Priority is for edit distance 0 , then 1, then 2. Else, defaults to the input word itself
    """

    # List of possible candidate words based on edit distances from the input word.
    # The resulting sets contain valid candidate words that could be potential replacements for the input word.
    # Prefers candidates with the smallest edit distance from the input word
    candidates = (known(edits0(word)) or known(edits1(word)) or known(edits2(word)) or [word])

    # The key argument specifies a one-argument ordering function like that used for list.sort()
    return max(candidates, key=WORD_COUNTS.get)


# EXAMPLE: Usage of the correct function
print(correct("mosnter"))


# Extend the function above to correct a word match in a case insensitive fashion

def correct_match(match):
    """Spell-correct word in match, and preserve proper upper/lower/title case
       :param match: object resulting from matching a regular expression with a word
    """

    word = match.group()

    def case_of(text):
        """Returns the case-function appropriate for the specified text"""

        return str.upper if text.isupper() else str.lower if text.islower() else str.title if text.istitle() else str

    # Note that case_of(word) returns a function that, applied to the corrected lower-case word,
    # restores its original capitalization
    return case_of(word)(correct(word.lower()))


def correct_text_generic(text):
    """Corrects all the words within a text, returning the corrected text"""

    return re.sub(r"[a-zA-Z0-9]+", correct_match, text)


# EXAMPLE: Usage of the case-insensitive, correct function

print(correct_text_generic("Hey FINAllLY We are goood to goo"))
