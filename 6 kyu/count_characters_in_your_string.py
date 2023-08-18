# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
# should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.


# MY SOLUTION

def count(s):

    dictionary = {}
    counter = ''

    for symbol in s:
        if symbol not in counter:
            dictionary[symbol] = s.count(symbol)
            counter += symbol

    return dictionary

# DEMONSTRATION

print(count('aabb'))
