# 10788 Reuters news documents, grouped into train and test sets
from nltk.corpus import reuters

# Get categories
print("Categories: {}...".format(
    reuters.categories()[0:10]))

# Get sentences in a set of categories
sentences = reuters.sents(categories=["coconut", "fuel"])

print("\nSentences: \n{}\n...".format(
    "\n".join(" ".join(sentence_tokens) for sentence_tokens in sentences[0:10])))

# File ID based access
fileIds = reuters.fileids(categories=["housing", "income"])
sentences_fileIds = reuters.sents(fileids=fileIds[0:2])
