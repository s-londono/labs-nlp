import nltk

# Import the Brown corpus
from nltk.corpus import brown

# Show the categories available in the Brown corpus
print("Total categories in the Brown corpus: {}".format(len(brown.categories())))
print("- {}".format("\n- ".join(brown.categories())))

# Tokenized senteces
brown.sents(categories="mystery")

# POS tagged senteces
print("\nPOS Tagged sentences: \n{}".format(
    brown.tagged_sents(categories="learned")))

# Get the nouns from the tagged words. Nouns are tagged as NN or NP.
# Note the use of a generator within the any function, thus the values 
# evaluated by any are generated as it iterates over the words and short-circuits 
# as it sees the first True value. (Some words have several tags. e.g. NN-HL!)
tagged_words = brown.tagged_words(categories="science_fiction")
nouns = [(word, tag) for word, tag in tagged_words if any(noun_tag in tag for noun_tag in ['NN', 'NP'])]

print("\nNouns: {}\n- {}".format(
    len(nouns),
    "\n- ".join((wt_pair[0] + ": " + wt_pair[1]) for wt_pair in nouns[0:20])))

# Build frequency distribution for nouns. (Note that using a generator instead of a comprehension 
# should have a positive effect in performance/memory footprint)
nouns_freq = nltk.FreqDist(word for word, tag in nouns)

print("\nFrequency distribution of nouns. Most common: \n{}".format(nouns_freq.most_common(10)))
