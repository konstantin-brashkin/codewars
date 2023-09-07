# Task
# Given a string str, reverse it and omit all non-alphabetic characters.
#
# Example
# For str = "krishan", the output should be "nahsirk".
#
# For str = "ultr53o?n", the output should be "nortlu".
#
# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.
#
# [output] a string


# MY SOLUTION

def reverse_letter(string):
    final_str = ''
    for i in string:
        if i.isalpha():
            final_str += i
    return final_str[::-1]


# DEMONSTRATION

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))
print(reverse_letter("ab23c"))
print(reverse_letter("krish21an"))
