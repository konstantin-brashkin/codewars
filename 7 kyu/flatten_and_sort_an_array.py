# Challenge:
#
# Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the
# sorted (ascending) order.
#
# Example:
#
# Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].


# MY SOLUTION

def flatten_and_sort(array):
    return sorted([i for arr in array for i in arr])


# DEMONSTRATION

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))
