import nltk
from pprint import pprint

# Manually create and use an instance of TreebankWordTokenizer

print("\n\n-- EXAMPLE 3: TEXT IN ENGLISH. MANUALLY INSTANTIATED TreebankWordTokenizer\n")

sentence = "The brown (suppossedly quick) fox was not so quick and couldn't jump over the dog."

tknzr = nltk.tokenize.TreebankWordTokenizer()

# convert_parenthesis set to True tokenizes ( as -LRB- and ) as -RRB-
words = tknzr.tokenize(sentence, convert_parentheses=False)

print("Sentence: \n'{}'\nwas split into words:\n".format(sentence))
pprint(words, indent=2)

# Regular expression tokenizer. The default pattern is: "\w+|\$[\d\.]+|\S+", with gaps=False, which means that the
# pattern recognizes tokens and not word separators

print("\n\n-- EXAMPLE 4: TEXT IN ENGLISH. MANUALLY INSTANTIATED RegexpTokenizer\n")

re_sentence = "This is a  very long      story, my friend    so..."

# This tokenizer will identify gaps between words, as gaps is set to True (note that r stands for raw string)
GAPS_PTTRN = r"\s+"

pre_tknzr = nltk.tokenize.RegexpTokenizer(pattern=GAPS_PTTRN, gaps=True)

re_words = pre_tknzr.tokenize(re_sentence)

print("Sentence: \n'{}'\nwas split into words:\n".format(re_sentence))
pprint(re_words, indent=2)

