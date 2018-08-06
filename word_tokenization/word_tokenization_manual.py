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
GAPS_PTTRN = r"\s|[\(\)]+"

re_tokenizer = nltk.tokenize.RegexpTokenizer(pattern=GAPS_PTTRN, gaps=True)

re_words = re_tokenizer.tokenize(re_sentence)

print("Sentence: \n'{}'\nwas split into words:\n".format(sentence))
pprint(re_words, indent=2)

# Demarcate tokens with start and end indices
word_indices = re_tokenizer.span_tokenize(sentence)

print("Sentence words as indices: \n")

pprint(["({},{}): {}".format(ws, we, sentence[ws:we]) for (ws, we) in word_indices], indent=2)

# Classes derived from RegexpTokenizer:
# - WordPunktTokenizer: uses the pattern \w+|[^\w\s]+
# - WhitespaceTokenizer: tokenizes sentences based including tabs, newlines, spaces, but better use split

print("\n\n-- EXAMPLE 5: TEXT IN ENGLISH. SPECIALIZATION OF RegexpTokenizer\n")

wrdpunkt_tokenizer = nltk.tokenize.WordPunctTokenizer()
wspace_tokenizer = nltk.tokenize.WhitespaceTokenizer()

wspace_words = wspace_tokenizer.tokenize(sentence)
wrdpunkt_words = wrdpunkt_tokenizer.tokenize(sentence)

print("Sentence split into words by spaces:\n")
pprint(wspace_words, indent=2)

print("Sentence split into words by word punktuation:\n")
pprint(wrdpunkt_words, indent=2)
