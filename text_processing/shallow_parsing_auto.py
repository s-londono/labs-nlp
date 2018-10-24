# Shallow Parsing: extracts meaningful chunks (phrases) from sentences.
from pattern.en import parsetree

sentence = "Three rings were given to the elves. Immortal, wisest and fairest of all beings. Seven were given to the " \
           "Dwarf Lords, who were great miners and craftsmen of the mountain holes and nine were given to the race of " \
           "men, who above all else, desire power."

tree = parsetree(sentence)

# Print the tree, which tags words with POS tags and uses the IOB (Inside Outside Beginning) notation for chunking:
# Beginning (B): token is the beginning of a chunk. Inside (I): token is inside a chunk.
# Outside (O): token does not belong to any chunk.
print(tree)

# Print each sentence contained into the tree and for each sentence, print its set of chunks (phrases)
for i, sentence_tree in enumerate(tree):
    print("{}.\t{}".format(i, sentence_tree.chunks))

# Depict each chunk (phrase) and its internal constituents (part of speech of the phrase and its words)
for i, sentence_tree in enumerate(tree):
    for j, chunk in enumerate(sentence_tree.chunks):
        print("{}.{:02d} {:4s}: {}".format(i, j, chunk.type, chunk))




