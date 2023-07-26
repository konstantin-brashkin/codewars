# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.
#
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

# MY SOLUTION

def longest(a1, a2):
    final_str = ''
    for element in a1:
        if element not in final_str:
            final_str += element
    for element in a2:
        if element not in final_str:
            final_str += element
    sorted_string = ''.join(sorted(final_str))
    return sorted_string

# DEMONSTRATION

print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))
