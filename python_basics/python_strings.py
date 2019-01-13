# Check for substrings in a string
s1 = "There is a way"
is_in_s1 = "way" in s1
print(is_in_s1)

# Indexing and slicing: strings are iterables
for c in s1:
    print(c)

# Indexing
print(s1[3])

# Backwards indexing: negative indices
print(s1[-1])

# Slicing
sub1 = s1[3:8]
sub2 = s1[3:]
sub3 = s1[:7]
sub4 = s1[::2] # Offset: 2
print(sub4)

# Joining a list of strings with a separating string
sj = ".-.".join(["Si", "vis", "pace"])
print(sj)

# C's printf style formatting
fs1 = "..%.2f..%d..%s" % (1.2323, 22, "text")
print(fs1)

# Format method (since 2.6) https://docs.python.org/2/library/string.html#formatstrings
fs2 = "..{:.2f}..{}..{t1}..{o2[1]}".format(1.44323, 22, t1="text2", o2=("p1", "p2"))
print(fs2)

