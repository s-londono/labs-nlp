# Lamba function as filter
a1 = [1, 2, 3, 4, 5]
a1_filtered = filter(lambda i: (i % 2) == 0, a1)
print("Pairs: {}".format([e for e in a1_filtered]))

# Lambda function as reducer
from functools import reduce
words = ["I", "am", "the", "truth", "the", "way", "and", "the", "life"]
sentence = reduce(lambda accum, w: " ".join([accum, w]), words)
print("{}".format(sentence))

# Iterables and iterators (how for loops work under the hood)
a = range(0, 10)
iter = iter(a)
while True:
    try:
        print("Cur item: {}".format(next(iter)))
    except StopIteration:
        break
else:
    print("Iteration loop properly broken")
    