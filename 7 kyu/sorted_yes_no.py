# Complete the method which accepts an array of integers, and returns one of the following:
#
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise
# You can assume the array will always be valid, and there will always be one correct answer.


# MY SOLUTION

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return 'yes, ascending'
    else:
        if arr == sorted(arr, reverse = True):
            return 'yes, descending'
        else:
            return 'no'


# DEMONSTRATION

print(is_sorted_and_how([1, 2]))
print(is_sorted_and_how([15, 7, 3, -8]))
print(is_sorted_and_how([4, 2, 30]))
