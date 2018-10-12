from nltk import word_tokenize
from nltk.corpus import treebank
from nltk.tag import DefaultTagger
from nltk.tag import RegexpTagger
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger
from nltk.classify import NaiveBayesClassifier
from nltk.tag.sequential import ClassifierBasedPOSTagger

# Load data from the treebank corpus to be used for evaluating the performance of taggers
data = treebank.tagged_sents()
train_data = data[:3500]
test_data = data[3500:]

print(train_data[0])
print(test_data[0])

sentence = "I remember stories of a glorious civilization of cities with spires that " \
           "reached to the sun. With myths of humanity everlasting and children who saw on " \
           "the embers of dying stars the destiny of their race."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Use the test data to evaluate taggers and see how they perform on the sample sentence.

# Build a custom tagger by extending class TaggerI, from the nltk.tag package and implementing the tag function.
# Use the evaluate function to assess the performance of the tagger.

# --- Tagger ---
# INPUT: Sentence tokens
# OUTPUT: List of pairs where each item corresponds to a token of the input with its POS tag

# 1. BACKOFF TAGGER (a tagger that is consulted by another when not able to tag a token):
#    Assigns the same tag to all tokens (tag specified as argument, NN in this case)
dt = DefaultTagger("NN")

# Measure accuracy on test data (i.e. Gold Standard). Test data should be tagged to compare these
# tags against new ones computed by the evaluated tagger (dt in this case)
print(dt.evaluate(gold=test_data))
print(dt.tag(tokens=tokens))

# 2. REGEX TAGGER:
#    Assigns tags to tokens by comparing their word strings to a series of regular expressions

# Define regex patterns used that determine the tags of tokens. Note that when tagging a token, expressions
# are evaluated bottom up and thus, the last one defines the default tag
patterns = [
    (r".*ing$", "VBG"),     # Gerunds
    (r".*ed$", "VBD"),      # Simple past
    (r".*es$", "VBZ"),      # 3rd singular present
    (r".*ould$", "MD"),     # Modals
    (r".*'s$", "NN$"),      # Possesive pronouns
    (r".*s$", "NNS"),       # Plural nouns
    (r"^-?[0-9]+(.[0-9]+)?$", "CD"),    # Cardinal numbers
    (r".*", "NN")           # Nouns (default)
]

rt = RegexpTagger(regexps=patterns)

print(rt.evaluate(test_data))
print(rt.tag(tokens))

# 3. N-GRAM TAGGERS:
#    Contiguous sequences of n items from a sequence of text or speech. Items can be words, phonemes,
#    letters, characters or syllabes. Shingles: n-grams where items are just words.
#    UnigramTagger -> NGramTagger -> ContextTagger -> SequentialBackoffTagger

# Train the N-Gram taggers using the training_data (pre-tagged tokens, i.e. labeled observations)
ut = UnigramTagger(train=train_data)
bt = BigramTagger(train_data)
tt = TrigramTagger(train_data)

# Test the performance of each N-Gram tagger
print("1-Gram Tagger Accuracy: {}".format(ut.evaluate(test_data)))
print("2-Gram Tagger Accuracy: {}".format(bt.evaluate(test_data)))
print("3-Gram Tagger Accuracy: {}".format(tt.evaluate(test_data)))

print("\n1-Gram tags:")
print(ut.tag(tokens))

print("\n2-Gram tags:")
print(bt.tag(tokens))

print("\n3-Gram tags:")
print(tt.tag(tokens))

# Note that the best accuracy is provided by the 1-Gram tagger, as it isn't always the case that the same bigrams
# and trigrams observed in the training data will be present in the same way in the testing data (e.g. pairs of words
# do not always appear paired in the same way)

# 4. TAGGER CHAINING WITH BACKOFF TAGGERS:


# Function to chain a set of taggers, with a backoff tagger as last resource
def combined_tagger(training_data, taggers, backoff=None):

    for tagger in taggers:
        backoff = tagger(training_data, backoff=backoff)

    return backoff


ct = combined_tagger(training_data=train_data, taggers=[UnigramTagger, BigramTagger, TrigramTagger], backoff=rt)

# Evaluate the chained tagger with backoff. (Great accuracy! 90.91%)
print(ct.evaluate(test_data))

print("\n4-Chained tags:")
print(ct.tag(tokens))


# 5. TAGGER TRAINED BY SUPERVISED CLASSIFICATION ALTGORITHM (Naive Bayes Classifier)
#    The feature_detector function forms the core of the training process. It generates features of the training data,
#    such as word, previous word, tag, previous tag, case etc.

nbt = ClassifierBasedPOSTagger(train=train_data, classifier_builder=NaiveBayesClassifier.train)

# Evaluate tagger on test data and sample sentence. (Awesome accuracy! 93.07%)
print(nbt.evaluate(test_data))

print("\n5-Naive Bayes Classifier-based tags:")
print(nbt.tag(tokens))

