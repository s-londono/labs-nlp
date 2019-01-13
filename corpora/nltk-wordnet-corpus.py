from nltk.corpus import wordnet as wn

# Word of interest
woi = "scorn"

# Get synsets for word of interest (synonyms and different meanings for the woi)
woi_synsets = wn.synsets(woi)
print("WOI: {}. Synsets: {}".format(woi, woi_synsets))

# Get details for each synonym in the synsets
for synset in woi_synsets:
    print("\nSynset {}. POS Tag: {}. Definition: {}".format(synset.name(), synset.pos(), synset.definition()))
    print("Examples: {}".format(synset.examples()))