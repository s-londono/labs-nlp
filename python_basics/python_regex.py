# Regex flags: re.I (re.IGNORECASE), re.S (re.DOTALL), re.U (re.UNICODE deprecated in 3)
import re
rx = re.compile(r"\W+|_+")      # Compile into regex object
mt = rx.match("%#$%$")          # Match patterns at the beginning of the string
ma = rx.search("as____,qp")     # Match patterns at any position of the string
mf = rx.search("as____,qp")     # Return all non-overlapping matches in the string

for m in rx.finditer("abc___de%%$_fk@!)aqw***"):        # Return all matched instances in form of an iterator
    print("- Match: " + m.string[m.start():m.end()])
    
sb = rx.sub("X", "aaa___kdj$#@#$__34kdqw*&#")   # Substitute all matches with a replacement string
print(sb)

# dealing with unicode matching
s = u"H\u00e8llo"

print(s)

# In Python 2, use the unicode flag to detect unicode chars, not necessary in Python 3
# print(re.findall(r"\w+", s), re.UNICODE) In Python 2
print(re.findall(r"\w+", s)) # In Python 3