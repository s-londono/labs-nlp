# Custom shallow parsing functions can be created using regular expressions and tagging-based learners

from nltk.chunk import RegexpParser
from pattern.en import tag

# Regex based Shallow Parsing using concepts of chunking and chinking (the reverse of chunking)
smple_sntnc = 'The quick brown fox jumped over the lazy dog'

# Get POS tagged sentence
tagged_smpl_sntnc = tag(smple_sntnc)

print(tagged_smpl_sntnc)

# Illustrate NP chunking based on explicit chunk patterns
chunk_grammar = """
NP: {<DT>?<JJ>*<NN.*>}
"""

# A. Chunking based parser:
# Create a new chunk parser, from the given start state and set of chunk patterns. Use it to shallow-parse the sentence
rc_u = RegexpParser(grammar=chunk_grammar)
c_u = rc_u.parse(tagged_smpl_sntnc)

# View NP chunked sentence using chunking
print(c_u)

# B. Chinking based parser:
# Illustrate NP chunking based on explicit chink patterns
chink_grammar = """
NP: {<.*>+} 
}<VBD|IN>+{
"""

rc_i = RegexpParser(chink_grammar)
c_i = rc_i.parse(tagged_smpl_sntnc)

# View NP chunked sentence using chinking
print(c_i)



