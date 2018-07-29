import math

# Create and consume a simple generator
def logGen(m):
    for x in m:
        yield math.log(x)

lg = logGen(range(1, 20))

print("Generator: {}".format(lg))
print("Generated: {}".format([i for i in lg]))

# Generator expression (looks like a comprehension in parentheses)
csv = "Tell, me, gentle, traveler, do, you, know, the, demon";
ge = (w.strip() for w in csv.split(","))
print("Sentence list: {}".format([e for e in ge]))

