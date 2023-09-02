# You'll be given a list of two strings, and each will contain exactly one colon (":") in the middle (but not at
# beginning or end). The length of the strings, before and after the colon, are random.
#
# Your job is to return a list of two strings (in the same order as the original list), but with the characters after
# each colon swapped.
#
# Examples
# ["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
# ["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]


# MY SOLUTION

def tail_swap(strings):

    first_split = strings[0].split(":")
    second_split = strings[1].split(":")

    first_final = ''.join(first_split[0] + ":" + second_split[1])
    second_final = ''.join(second_split[0] + ":" + first_split[1])

    return [first_final, second_final]


# DEMONSTRATION

print(tail_swap(['abc:123', 'cde:456']))
print(tail_swap(['a:12345', '777:xyz']))
print(tail_swap(['MbVjBR^Z!:EM!1bL&', 'mv:Jb1e%Q']))
