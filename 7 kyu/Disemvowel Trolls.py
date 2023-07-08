# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the
# threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.


# MY SOLUTION

def disemvowel(string_):
    vowels = 'aeiou'
    final_string = ""
    for letter in string_:
        if letter.lower() not in vowels:
            final_string += letter
    return final_string


# DEMONSTRATION

print(disemvowel("This website is nice!"))