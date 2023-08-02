# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the
# string should be retained.
#
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"


# MY SOLUTION

def reverse_words(text):
    words = text.split()
    final_str = ''
    if text.count(" ") < len(words):
        for word in words:
            final_str += ''.join(reversed(word)) + " "
    elif text.count(" ") >= len(words):
        for word in words:
            final_str += ''.join(reversed(word)) + "  "

    return final_str.rstrip()


# DEMONSTRATION
print(reverse_words('elbuod  decaps  sdrow'))
