from pattern.en import suggest
from aspell import Speller

# The algorithm manually implemented at spelling_correction_manual.py is available to be
# used out of the box in the pattern library:
# https://www.clips.uantwerpen.be/pattern.
# (Compatible with python 2.7 only)
#
# "Pattern is a web mining module for the Python programming language.
#  It has tools for data mining (Google, Twitter and Wikipedia API, a web crawler, a HTML DOM parser),
#  natural language processing (part-of-speech taggers, n-gram search, sentiment analysis, WordNet),
#  machine learning (vector space model, clustering, SVM), network analysis and <canvas> visualization."

# Other libraries are:
# PyEnchant: http://pythonhosted.org/pyenchant/
# AspellPython, wrapper around GNU Aspell: https://github.com/WojciechMula/aspell-python (requires libaspell-dev)
#   sudo apt install libaspell-dev
#   pip install aspell-python-py3

print(suggest("fianlly"))

print(suggest("flaot"))

sp = Speller()
print(sp.suggest("fianlly"))