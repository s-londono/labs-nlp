# Flatten list with comprehensions
cl = [[1, 2, 3, 4], ["a", "b", "c"], [0.1, 0.2, 0.3, 0.4]]
fl = [i for lst in cl for i in lst]
print("Flattened list: {}".format(fl))

# Dictionary comprehension
l1 = range(0, 10)
d1 = {str(i + r): r for i in l1 if i % 2 == 0 for r in range(0, i)}
print("Pair squares: {}".format(d1))