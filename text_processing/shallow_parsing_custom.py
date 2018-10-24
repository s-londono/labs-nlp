# Custom shallow parsing functions can be created using regular expressions and tagging-based learners

from nltk.corpus import treebank_chunk

# Training data points used here are sentences already annotated with phrase and POS tags
data = treebank_chunk.chunked_sents()

train_data = data[:4000]
test_data = data[4000:]

print(train_data[7])

# Regex based Shallow Parsing using concepts of chunking and chinking (the reverse of chunking)

