import nltk
from nltk.corpus import gutenberg
from pprint import pprint
# from nltk.tokenize.punkt import PunktSentenceTokenizer
# from random import sample

# Load the Alice in Wonderland corpus
alice = gutenberg.raw(fileids="carroll-alice.txt")

# Create a test corpus
sample_text = "We will discuss briefly about the basic syntax, structure and design philosophies. " + \
    "There is a defined hierarchical syntax for Python code which you should remember when " + \
    "writing code! Python is a really powerful programming language!"
    
print("Total characters in Alice in Wonderland corpus: {}".format(len(alice)))
print("\n")

print("First 100 chars. in corpus: \n{}".format(alice[0:100]))
print("\n")

# Use the recommended sentence tokenization function provided by NLTK. Uses an instance of PunktSentenceTokenizer  
# that has been pre-trained on several languages and works really well
default_st = nltk.sent_tokenize

# Tokenize the corpora in sentences
alice_sentences = default_st(text=alice)
sample_sentences = default_st(text=sample_text)

print("Total sentences in sample: {}".format(len(sample_sentences)))
print("Total sentences in Alice: {}".format(len(alice_sentences)))
print("\n")

print("Sample text sentences :-")
pprint(sample_sentences)
print("\n")

print("Alice sentences (first 5) :-")
pprint(alice_sentences[0:5])
print("\n")

# Tokenize text in other languages
from nltk.corpus import europarl_raw


print("Available files in German :-")
pprint(europarl_raw.german.fileids())
print("\n")

german_text = europarl_raw.german.raw(fileids="ep-00-01-17.de")

# Use a default sentence tokenizer for German to tokenize the text
german_sentences_default = default_st(text=german_text, language="german")

# Create a pre-trained tokenizer specialized for the German language. PunktSentenceTokenizer instance
german_punkt_tokenizer = nltk.data.load(resource_url="tokenizers/punkt/german.pickle")
print(type(german_punkt_tokenizer))

german_sentences = german_punkt_tokenizer.tokenize(german_text)

print("Are sentences obtained from both tokenizers the same? {}".format(german_sentences_default == german_sentences))

for i in range(0, 5):
    print(german_sentences[i])

print("\n")

# Using the default, generic PunktSentenceTokenizer class (uses an usupervised algorithm to detect sentences):
punkt_st = nltk.tokenize.PunktSentenceTokenizer()

sample_sentences = punkt_st.tokenize(sample_text)

print("Sample sentences (using generic PunktSentenceTokenizer):")
pprint(sample_sentences)

print("\n")

# Regex-based sentence tokenizer
# Note the usage of (?<=...), positive lookback assertions and (?<!...), negative lookback assertions
SENTENCE_TOKENS_PATTERN = r"(?<!\w\.\w\.)(?<![A-Z][a-z]\.)(?<![A-Z]\.)(?<=\.|\?|\!)\s"

regex_st = nltk.tokenize.RegexpTokenizer(pattern=SENTENCE_TOKENS_PATTERN, gaps=True)

sample_sentences = regex_st.tokenize(sample_text)

print("Sample sentences (using RegexpTokenizer):")
pprint(sample_sentences)

print("\n")



