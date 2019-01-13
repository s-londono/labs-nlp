from nltk.corpus import treebank_chunk
from nltk.corpus import conll2000
from nltk.chunk.util import tree2conlltags, conlltags2tree
from nltk.tag import UnigramTagger, BigramTagger
from nltk.chunk import ChunkParserI
from pattern.en import tag

# Training data points used here are sentences already annotated with phrase and POS tags
data = treebank_chunk.chunked_sents()

train_data = data[:4000]
test_data = data[4000:]

# -- Basics: usage of functions

# Sample training sentence
train_sent = train_data[7]
print(train_sent)

# Get the (word, POS tag, Chunk tag) triples for each token. Or more formally,
# Return a list of 3-tuples containing (word, tag, IOB-tag). Convert a tree to the CoNLL IOB tag format.
wtc = tree2conlltags(train_sent)
print(wtc)

# Build a shallow parsed tree back from the WTC triples. That is, convert the CoNLL IOB format to a tree.
test_tree = conlltags2tree(wtc)
print(test_tree)


# -- Implementation: function to train taggers

# Extract POS and chunk tags from a collection of sentences, given as syntax trees.
# Transforms a collection of syntax trees (nltk.tree.Tree instances) into a list of lists of tuples (tag, IOB-tag).
# Each element of the resulting list represents a sentence, corresponding to one of the syntax trees
# provided as argument. Each one of these lists contains the POS tags and IOB-tags (chunk tags)
# of its words, as a list of tuples (tag, IOB-tag)
def conll_tag_chunks(chunk_sents):

    tagged_sents = [tree2conlltags(tree) for tree in chunk_sents]

    return [[(t, c) for (w, t, c) in sent] for sent in tagged_sents]


# Chains a collection of taggers by iteratively wrapping them up as backoff of the previous one. The last tagger in the
# collection of taggers will be the one put upfront of the chain
def combined_tagger(train_d, taggers, backoff=None):

    for tagger in taggers:
        backoff = tagger(train_d, backoff=backoff)

    return backoff


# Class NGramTagChunker: takes in tagged sentences as training input, get their (word, POS tag, Chunk tag) WTC triples
# and train a BigramTagger with a UnigramTagger as backoff tagger. The parse function performs shallow parsing on
# new sentences
class NGramTagChunker(ChunkParserI):

    # Constructor. Trains the shallow parser using n-gram tagging based on the WTC triples for each sentence.
    # Takes a list of training sentences as input, which is annotated with chunked parse tree metadata
    def __init__(self, train_sentences, tagger_classes=[UnigramTagger, BigramTagger]):

        # For each training chunked parse tree, get the list of POS Tag - Chunk Tag tuples
        train_sent_tags = conll_tag_chunks(train_sentences)

        # Train BigramTagger with UnigramTagger as backoff using the POS Tag - Chunk Tag triples
        self.chunk_tagger = combined_tagger(train_sent_tags, tagger_classes)

    # Uses the trained Chunk Tagger to shallow parse new sentences. Takes a POS-tagged sentence as input
    def parse(self, tagged_sentence):

        if not tagged_sentence:
            return None

        # Separate out POS tags from the sentence
        pos_tags = [tag for word, tag in tagged_sentence]

        # Use the chunk tagger to get IOB Tags (Chunk Tags) for the sentence, using the POS Tags of its words as input
        chunk_pos_tags = self.chunk_tagger.tag(pos_tags)

        chunk_tags = [chunk_tag for (pos_tag, chunk_tag) in chunk_pos_tags]

        # Combine the obtained IOB Tags with the Words and POS Tags to form WTC triples
        wpc_tags = [(word, pos_tag, chunk_tag) for ((word, pos_tag), chunk_tag) in zip(tagged_sentence, chunk_tags)]

        # Build the shallow parse tree from the WTC triples of the sentence
        return conlltags2tree(wpc_tags)


# -- Tests

# Train the shallow parser
ntc = NGramTagChunker(train_data)

# Test the performance of the shallow parser on test data
print(ntc.evaluate(test_data))

# Parse a sentence
smple_sntnc = 'The brown fox is quick and he is jumpling over the lazy dog'

# Create POS tagged tokens from sample sentence
tagged_sentence = tag(smple_sntnc)

tree = ntc.parse(tagged_sentence)

print(tree)

# -- PART II: Train the shallow parser on the Conll2000 corpus, which contains excerpts from the Wall Street Journal
# and is much larger than treebank_chunk

wsj_data = conll2000.chunked_sents()

# Train the parser on the first 7500 sentences, test on the rest
train_wsj_data = wsj_data[:7500]
test_wsj_data = wsj_data[7500:]

print(train_wsj_data[10])

# Train the shallow parser
tc = NGramTagChunker(train_wsj_data)

# Test performance on the test data
print(tc.evaluate(test_wsj_data))


