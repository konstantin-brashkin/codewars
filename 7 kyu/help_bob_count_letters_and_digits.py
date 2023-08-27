# Bob is a lazy man.
#
# He needs you to create a method that can determine how many letters (both uppercase and lowercase ASCII letters)
# and digits are in a given string.
#
# Example:
#
# "hel2!lo" --> 6
#
# "wicked .. !" --> 6
#
# "!?..A" --> 1


# MY SOLUTION

def count_letters_and_digits(s):
    counter = 0
    for symbol in s:
        if symbol.isdigit() or symbol.isalpha():
            counter += 1

    return counter

# DEMONSTRATION

print(count_letters_and_digits('n!!ice!!123'))
print(count_letters_and_digits('de?=?=tttes!!t'))

