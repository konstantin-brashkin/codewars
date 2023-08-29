# Write a function that accepts a string, and returns true if it is in the form of a phone number.
# Assume that any integer from 0-9 in any of the spots will produce a valid phone number.
#
# Only worry about the following format:
# (123) 456-7890 (don't forget the space after the close parentheses)
#
# Examples:
#
# "(123) 456-7890"  => true
# "(1111)555 2345"  => false
# "(098) 123 4567"  => false


# MY SOLUTION

from itertools import chain


def valid_phone_number(phone_number):
    test_bool = True

    if len(phone_number) != 14:
        test_bool = False

    try:
        if (phone_number[0] != '(') or (phone_number[4] != ')' or (phone_number[5] != " ") or (phone_number[9] != '-')):
            test_bool = False
    except IndexError:
        test_bool = False

    try:
        for i in chain(range(1, 4), range(6, 9), range(10, 14)):
            if not phone_number[i].isdigit():
                test_bool = False
    except IndexError:
        test_bool = False

    return test_bool


# DEMONSTRATION
print(valid_phone_number('fds'))
print(valid_phone_number("(123) 456-7890"))
print(valid_phone_number("(1111)555 2345"))
print(valid_phone_number("abc(123)456-7890"))
