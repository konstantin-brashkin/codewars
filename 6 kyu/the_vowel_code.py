# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers
# according to the following pattern:
#
# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
#
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern
# shown above.
#
# For example, decode("h3 th2r2") would return "hi there".
#
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


# MY SOLUTION

def encode(st):
    encryption = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    final_str = ''
    for symbol in st:
        if symbol in encryption:
            final_str += encryption[symbol]
        else:
            final_str += symbol
    return final_str


def decode(st):
    decryption = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    final_str = ''
    for symbol in st:
        if symbol in decryption:
            final_str += decryption[symbol]
        else:
            final_str += symbol
    return final_str

# DEMONSTRATION


print(encode('How are you today?'))
print(decode('h2ll4'))
