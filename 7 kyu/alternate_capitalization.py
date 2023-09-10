# Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown
# below. Index 0 will be considered even.
#
# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.
#
# The input will be a lowercase string with no spaces.
#
# Good luck!


# MY SOLUTION

def capitalize(s):
    even_str = ''.join(s[i].upper() if i % 2 == 0 else s[i].lower() for i in range(len(s)))
    odd_str = ''.join(s[i].lower() if i % 2 == 0 else s[i].upper() for i in range(len(s)))
    return [even_str, odd_str]


# DEMONSTRATION

print(capitalize("abcdef"))
print(capitalize("codewars"))
print(capitalize("abracadabra"))
print(capitalize("codewarriors"))
