from nltk.corpus import treebank_chunk
from nltk.chunk import RegexpParser
from pattern.en import tag

# Training data points used here are sentences already annotated with phrase and POS tags
data = treebank_chunk.chunked_sents()

train_data = data[:4000]
test_data = data[4000:]

print(train_data[7])

# Regex-based shallow parser.
# The Tree structures used to represent parsed sentences in NLTK get converted to ChunkString objects here.
# Create an object RegexpParser using chunking and chunking rules (classes ChunkRule and ChinkRule)

smple_sntnc = 'The brown fox is quick and he is jumpling over the lazy dog'

# Create POS tagged tokens from sample sentence
tagged_sentence = tag(smple_sntnc)

print(tagged_sentence)

# Create the shallow parser
grammar = """
NP: {<DT>?<JJ>?<NN.*>}
ADJP: {<JJ>}
ADVP: {<RB.*>}
PP: {<IN>}
VP: {<MD>?<VB.*>+}
"""

rc = RegexpParser(grammar)

# Shallow parse the sample sentence
c = rc.parse(tagged_sentence)
print(c)

# Evaluate parser performance on test data
print(rc.evaluate(test_data))

