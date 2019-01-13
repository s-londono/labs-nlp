# INSTALLATION OF DEPENDENCIES
#
# All corpora associated to NLTK:
# - nltk.download('all', halt_on_error=false)
#
# Pattern library:
# - /home/slondono/software/anaconda2/bin/conda install pattern
#
# Spacy.io, for tagging and depicting dependency-based parsing:
# - /home/slondono/software/anaconda2/bin/conda install -c conda-forge spacy
#
# Spacy models and laguages. Can be installed as Python packages:
# - source /home/slondono/software/anaconda2/bin/activate nlp2
# - python -m spacy download en
# - python -m spacy download es
# - python -m spacy download de
#
# Spacy. To load a language:
# - import spacy
# - nlp = spacy.load('de')
#
# Stanford Parser, performs constituency and dependency grammar-based parsing.
# Implemented in Java, but NLTK provides a wrapper to use it from Python
# https://nlp.stanford.edu/software/lex-parser.shtml
# https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software
#
# GraphViz and PyGraphviz, to visualize the dependency parse tree generated by the Stanford Parser:
# http://www.graphviz.org/download/
#
#
from nltk import word_tokenize
from nltk import pos_tag
from nltk import pos_tag_sents
from pattern.en import tag

# 1. POS Tagging using NLTK

sentence = "The brown fox is quick and he is jumping over the lazy dog"

lst_sentences = ["En algún lugar de La Mancha, de cuyo nombre no quiero acordarme",
                 "Muchos años después, ante el pelotón de fusilamiento, el coronel Aureliano Buendía recordaría",
                 "Los Aimaras vivían en paz en Tihuanaco. Hasta que un día llegó un hombre rubio"]

tokens = word_tokenize(sentence)
tagged_sent = pos_tag(tokens, lang="eng")

# Use pos_tag_sents to efficiently tag more than one sentence
lst_tokens = [word_tokenize(sntnc) for sntnc in lst_sentences]
lst_tagged_sents = pos_tag_sents(lst_tokens, lang="spa")

# 2. POS Tagging using the Pattern library. Resulting tags follow the Penn Treebank format
tagged_sent = tag(sentence)
print(tagged_sent)
