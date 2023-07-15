# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to
# match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


# MY SOLUTION

def scramble(s1, s2):
    final = True

    for_test_s2 = ''
    for element in s2:
        if element not in for_test_s2:
            for_test_s2 += element

    for element in for_test_s2:
        if s2.count(element) > s1.count(element):
            final = False

    return final

# DEMONSTRATION

print(scramble("scriptingjava", "javascript"))

