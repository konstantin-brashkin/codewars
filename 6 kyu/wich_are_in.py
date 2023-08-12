# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which
# are substrings of strings of a2.
#
# Example 1:
# a1 = ["arp", "live", "strong"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns ["arp", "live", "strong"]
#
# Example 2:
# a1 = ["tarp", "mice", "bull"]
#
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
#
# returns []
#
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.


# MY SOLUTION

def in_array(array1, array2):
    final_arr = []
    for i in range(0, len(array1)):
        for element in array2:
            if (element.find(array1[i]) != -1) and (array1[i] not in final_arr):
                final_arr.append(array1[i])
            else:
                pass
    return sorted(final_arr)


# DEMONSTRATION

print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
