# Write a method (or function, depending on the language) that converts a string to camelCase, that is,
# all words must have their first letter capitalized and spaces must be removed.
#
# Examples (input --> output):
# "hello case" --> "HelloCase"
# "camel case word" --> "CamelCaseWord"
# Don't forget to rate this kata! Thanks :)


# MY SOLUTION

def camel_case(s):
    words = s.split()
    final_str = ''
    for word in words:
        final_str += word.title()
    return final_str


# DEMONSTRATION

print(camel_case(" camel case word"))
