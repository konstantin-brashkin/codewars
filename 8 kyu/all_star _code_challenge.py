# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences
# the 2nd argument is found in the first one.
#
# If no occurrences can be found, a count of 0 should be returned.
#
# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0


# THE EASIEST SOLUTION

def str_count(strng, letter):
    return strng.count(letter)


# EXTENDED SOLUTION:

def str_count(strng, letter):
    counter = 0
    for symbol in strng:
        if symbol == letter:
            counter += 1
    return counter


# DEMONSTRATION


print(str_count('\nHello', 'o'))
print(str_count('\nHello', 'l'))
print(str_count('\nHello', 'a'))
