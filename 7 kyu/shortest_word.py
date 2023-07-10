# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.


# MY SOLUTION

def find_short(s):
    min_length = len(s.split()[0])
    for word in s.split():
        if len(word) < min_length:
            min_length = len(word)
    return min_length


# DEMONSTRATION

print(find_short("bitcoin take over the world maybe who knows perhaps"))
