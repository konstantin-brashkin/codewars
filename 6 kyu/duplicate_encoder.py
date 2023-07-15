# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
# that character appears only once in the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples "din"      =>  "(((" "recede"   =>  "()()()" "Success"  =>  ")())())" "(( @"     =>  "))((" Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
# the "XXX" is the expected result, not the input!


# MY SOLUTION

def duplicate_encode(word):
    final_str = ''
    for element in word.lower():
        test = word.lower().count(element)
        if test > 1:
            final_str += ')'
        else:
            final_str += '('
    return final_str


# DEMONSTRATION

print(duplicate_encode("Success"))
