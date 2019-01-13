# The process of lemmatization is very similar to stemming: removes word affixes to get a root word (not a root stem).
# In contrast with a root stem, a root word is always a lexicographically correct word (i.e. is in the dictionary).
# Root words are known as lemmas.

# The NLTK lemmatization module uses WordNet as dictionary, part-of-speech and context to get the lemma.
# (Parts of speech: mainly three entities, nouns, verbs and adjectives). Uses the morphy() function, part of the
# WordNetCorpusReader class

from nltk.stem import WordNetLemmatizer

# Returns the input word character if not found in WordNet. The part-of-speech (noun, verb, adjective) is
# extremely important for this lemmatizer to work effectively
wnl = WordNetLemmatizer()

# The second argument, n, means noun
print(wnl.lemmatize("cars", "n"))

# The second argument, v, means verb
print(wnl.lemmatize("running", "v"))
print(wnl.lemmatize("ate", "v"))
print(wnl.lemmatize("bought", "v"))

# Lemmatize adjectives
print(wnl.lemmatize("saddest", "a"))
print(wnl.lemmatize("fancier", "a"))

