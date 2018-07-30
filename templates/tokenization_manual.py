import nltk
from pprint import pprint
from nltk.corpus import europarl_raw

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
