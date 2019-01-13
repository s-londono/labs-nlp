import nltk
from pprint import pprint

# - Goal: split a sentence into a list of words that can be used to reconstruct the sentence
# - Word tokenization is the basis for other cleaning processes such as Stemming and Lemmatization.
# - Default and recommended word tokenizer: nltk.word_tokenize (wraps an instance of TreebankWordTokenizer).
# - TreebankWordTokenizer: based in the Penn Treebank (www.cis.upenn.edu/~treebank/tokenizer.sed)
#   - Splits and separates most punctuation characters into independent tokens.
#   - Splits words with standard contractions (e.g. don't -> do, n't)

print("\n\n-- EXAMPLE 1: TEXT IN ENGLISH. DEFAULT WRAPPER FUNCTION word_tokenize\n")

sentence = "The brown quick fox was not so quick and couldn't jump over the dog."

words = nltk.word_tokenize(sentence, language='english', preserve_line=False)

print("Sentence: \n'{}'\nwas split into words:\n".format(sentence))
pprint(words, indent=2)

print("\n\n-- EXAMPLE 2: TEXT IN SPANISH. DEFAULT WRAPPER FUNCTION word_tokenize\n")

sp_sentence = "Muchos años más tarde, frente al pelotón de fusilamiento, el coronel Aureliano Buendía " \
    "recordaría el día en que su padre lo llevó a conocer el hielo."

sp_words = nltk.word_tokenize(sp_sentence, language='english', preserve_line=False)

print("Spanish sentence: \n'{}'\nwas split into words:\n".format(sp_sentence))
pprint(sp_words, indent=2)
