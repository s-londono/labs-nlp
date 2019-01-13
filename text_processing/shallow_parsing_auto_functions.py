# Generic functions to parse and visualize shallow-parsed sentence trees
from pattern.en import parsetree, Chunk
from nltk.tree import Tree


# Create a shallow parsed sentece tree
def create_sentence_tree(sentence, lemmatize=False):

    sentence_tree = parsetree(sentence, relations=True, lemmata=lemmatize)

    return sentence_tree[0]


# Get various consituents of the parse tree
def get_sentence_tree_constituents(sentence_tree):

    return sentence_tree.constituents()


# Process the shallow parsed tree into an easy to understand format
def process_sentence_tree(sentence_tree):

    tree_cnstns = get_sentence_tree_constituents(sentence_tree)

    processed_tree = [(item.type, [(w.string, w.type) for w in item.words]) if type(item) == Chunk else
                      ('-', [(item.string, item.type)]) for item in tree_cnstns]

    return processed_tree


# Build the sentence tree using NLTK's tree syntax
def build_sentence_tree(sentence_tree):

    processed_tree = process_sentence_tree(sentence_tree)

    processed_tree = [Tree(item[0], [Tree(x[1], [x[0]]) for x in item[1]]) for item in processed_tree]

    return Tree("S", processed_tree)


# Print the sentence tree using NLTK's tree syntax
def print_sentence_tree(sentence_tree):

    tree = build_sentence_tree(sentence_tree)

    print(tree)


# Visualize the sentence tree using NLTK's tree syntax
def visualize_sentence_tree(sentence_tree):

    tree = build_sentence_tree(sentence_tree)

    tree.draw()


# Try the functions out
if __name__ == "__main__":

    sample = "Three rings were given to the elves. Immortal, wisest and fairest of all beings. Seven were given to " \
               "the Dwarf Lords, who were great miners and craftsmen of the mountain holes and nine were given to " \
               "the race of men, who above all else, desire power."

    t = create_sentence_tree(sample)

    print(t)

    pt = process_sentence_tree(t)

    print_sentence_tree(t)

    visualize_sentence_tree(t)
