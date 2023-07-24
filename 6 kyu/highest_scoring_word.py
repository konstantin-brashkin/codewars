# Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.


# MY SOLUTION

import string


def high(x):
    alphabet_lowercase = string.ascii_lowercase
    words = x.split()
    counter = []
    for word in words:
        temp_counter = 0
        for i in word:
            temp_counter += alphabet_lowercase.index(i) + 1
        counter.append(temp_counter)

    return words[counter.index(max(counter))]


# DEMONSTRATION

print(high('man i need a taxi up to ubud'))

