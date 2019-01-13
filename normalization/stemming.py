# Morphemes consist of units that are stems and affixes (prefixes, suffixes, etc.)
# Word stems are also known as base forms. Inflection creates new words by attaching
# affixes to stems. The reverse of this, obtaining the base form of a word from
# its inflected form is known as Stemming

# NLTK provides several implementations of stemmers in the stem module.
# Choose a stemmer based on the problem at hand and after trial and error

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.stem import SnowballStemmer

# PORTER STEMMER:
# Is the most frequently used stemmer
# http://www.tartarus.org/~martin/PorterStemmer

ps = PorterStemmer()

print(ps.stem("jumping"))
print(ps.stem("strange"))
print(ps.stem("lying"))

# LANCASTER STEMMER (a.k.a. Paice/Husk)
# Iterative stemmer, with over 120 rules for removal or replacement of affixes

ls = LancasterStemmer()

print(ls.stem("jumping"))
print(ls.stem("jumps"))
print(ls.stem("jumper"))
print(ls.stem("strange"))
print(ls.stem("stranger"))
print(ls.stem("lying"))

# REGEXP STEMMER
# Uses regular expressions to identify the morphological affixes in words and any part of the
# string matching the same is removed

# Note that this stemmer is case sensitive (won't work on capitalized affixes)
rs = RegexpStemmer(r"ing$|s$|ed$", min=4)

print(rs.stem("jumping"))
print(rs.stem("colored"))
print(rs.stem("lying"))

# SNOWBALL STEMMER
# Stems words in a dozen of languages. http://snowballstem.org

ss = SnowballStemmer(language="german")

print("Supported languages: {}".format(SnowballStemmer.languages))

print(ss.stem("autobahnen"))
print(ss.stem("endlich"))
print(ss.stem("unglaublich"))
print(ss.stem("untergehen"))
print(ss.stem("hauschen"))
