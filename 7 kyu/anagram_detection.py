# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
#
# Note: anagrams are case insensitive
#
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
#
# Examples
# "foefet" is an anagram of "toffee"
#
# "Buckethead" is an anagram of "DeathCubeK"


# MY SOLUTION

def is_anagram(test, original):
    test_format = ''.join(sorted(test.lower()))
    original_format = ''.join(sorted(original.lower()))
    return True if test_format == original_format else False


# DEMONSTRATION

print(is_anagram("foefet", "toffee"))
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("ound", "round"))
print(is_anagram("apple", "Pale"))
