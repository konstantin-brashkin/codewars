# Write a function that takes an array of strings as an argument and returns a sorted array containing the same
# strings, ordered from shortest to longest.
#
# For example, if this array were passed as an argument:
#
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
#
# Your function would return the following array:
#
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
#
# All of the strings in the array passed to your function will be different lengths, so you will not have to decide
# how to order multiple strings of the same length.


# MY SOLUTION

def sort_by_length(arr):
    final_arr = []

    while arr:
        final_arr.append(min(arr, key = len))
        arr.remove(min(arr, key = len))

    return final_arr


# DEMONSTRATION

print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))
