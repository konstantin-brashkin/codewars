# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.


# MY SOLUTION

def get_count(sentence):
    vowels = 'aeiou'
    counter = 0
    for letter in sentence:
        if letter in vowels:
            counter += 1
    return counter


# DEMONSTRATION

print(get_count('aeiou'))
print(get_count('y'))
print(get_count('hood'))

