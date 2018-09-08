import re
from nltk.corpus import wordnet
from nltk import word_tokenize

# Function to deal with incorrect tokens that have repeated characters and by just removing the duplicates,
# the token would be semantically correct


def remove_repeated_characters(tokens):

    repeated_pattern = re.compile(r"(\w*)(\w)\2(\w*)")

    match_substitution = r"\1\2\3"

    def replace(old_word):
        if wordnet.synsets(old_word):
            return old_word

        new_word = repeated_pattern.sub(match_substitution, old_word)

        return replace(new_word) if new_word != old_word else new_word

    return [replace(token) for token in tokens]


print(remove_repeated_characters(["finalllly", "hoooomeee", "caaarrr", "aiiirrr", "ssstriiiikkkeee", "offffer"]))

print(remove_repeated_characters(word_tokenize("The colonel said: aiir striiikeee, taaaakkkeee cooovvveeer")))








