import nltk
from pprint import pprint
from nltk.corpus import reuters

# Option 4: use a brand new, default RegExpTokernizer
print("\n\n-- EXAMPLE 5: TEXT IN ENGLISH. DEFAULT, NEWLY CREATED REGEXP SENTENCE TOKENIZER\n")

fuel_sentences = reuters.sents(categories=["fuel"])
sample_reuters = " ".join([wrd for sent in fuel_sentences[0:5] for wrd in sent])

print("Sentence: '{}'".format(sample_reuters))

# Regex-based sentence tokenizer
# Note the usage of (?<=...), positive lookback assertions and (?<!...), negative lookback assertions
SENTENCE_TOKENS_PATTERN = r"(?<!\w\.\w\.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)(?<=\.|\?|\!)\s"

regex_tokenizer = nltk.tokenize.RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True)

reuters_sentences = regex_tokenizer.tokenize(sample_reuters)

print("Text tokenized with: {}.\nTotal sentences: {}\n\nSample sentences>\n"
      .format(type(regex_tokenizer), len(reuters_sentences)))

pprint(reuters_sentences)

