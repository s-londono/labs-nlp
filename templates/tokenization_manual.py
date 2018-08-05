import nltk
from pprint import pprint
from nltk.corpus import europarl_raw
from nltk.corpus import reuters

german_text = europarl_raw.german.raw(fileids='ep-00-01-17.de')
print("Euro Parlament German text. Total length: {}".format(len(german_text)))
pprint(german_text[2:150], width=80)

# Option 2: manually load a PunktSentenceTokenizer pre-trained for the German language
print("\n\n-- EXAMPLE 3: TEXT IN GERMAN. LOADED PRE-TRAINED PUNKTUATION SENTENCE TOKENIZER\n")

german_punkt_tokenizer = nltk.data.load(resource_url="tokenizers/punkt/german.pickle")

german_sentences = german_punkt_tokenizer.tokenize(german_text)

print("Text tokenized with: {}.\nTotal sentences: {}.\n\nSample sentences:\n"
      .format(type(german_punkt_tokenizer), len(german_sentences)))

pprint(german_sentences[0:20])

# Option 3: use a brand new, default PunktSentenceTokenizer
print("\n\n-- EXAMPLE 4: TEXT IN ENGLISH. DEFAULT, NEWLY CREATED PUNKTUATION SENTENCE TOKENIZER\n")

fuel_sentences = reuters.sents(categories=["fuel"])
sample_reuters = " ".join([wrd for sent in fuel_sentences[0:5] for wrd in sent])

print("Sentence: '{}'".format(sample_reuters))

punkt_st = nltk.tokenize.PunktSentenceTokenizer()

reuters_sentences = punkt_st.tokenize(sample_reuters)

print("Text tokenized with: {}.\nTotal sentences: {}\n\nSample sentences>\n"
      .format(type(punkt_st), len(reuters_sentences)))

pprint(reuters_sentences)

