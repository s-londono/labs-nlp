import spacy
from spacy.pipeline import DependencyParser

nlp = spacy.load("en")

# Sample sentence
sentence = "The brown fox is quick and he is jumpling over the lazy dog"

parsed_sent = nlp(unicode(sentence))

print(parsed_sent)

# Generate the dependency parser output
#dependency_pattern = '{left}<---{word}[{w_type}]--->{right}\n--------'