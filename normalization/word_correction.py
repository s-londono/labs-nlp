import re

# 1. DROP REPEATED CHARACTERS: NON-GREEDY QUANTIFIER VERSION

# Python regex special sequence \2: matches the contents of the second group,
# that is (\w)\2 matches any repeating word character. Notices the usage of the non-greedy version of * )(*?)
# to prevent the first group from eating up the first repeated characters
repeat_pattern = re.compile(r"(\w*?)(\w)\2+(\w*)")

match_substitution = r"\1\2\3"

# Note that with sub: backreferences, such as \1, are replaced with the substring matched by group 6 in the pattern.
result = repeat_pattern.sub(match_substitution, "abcdddddddefg")

print("Result (non-greedy version): {}".format(result))

# 2. DROP REPEATED CHARACTERS: ITERATIVE VERSION (TEXT BOOK)

repeat_pattern_ii = re.compile(r"(\w*)(\w)\2(\w*)")

result = None
old_word = "abcdddddddefg"

step = 1

while True:

    new_word = repeat_pattern_ii.sub(match_substitution, old_word)

    if new_word != old_word:
        print("Step: {}. Word: {}".format(step, new_word))
        old_word = new_word

    else:
        print("Final word: {}".format(new_word))
        result = new_word
        break

    step += 1

print("Result (non-greedy version): {}".format(result))
