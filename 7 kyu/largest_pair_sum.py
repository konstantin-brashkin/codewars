# Given a sequence of numbers, find the largest pair sum in the sequence.
#
# For example
#
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.


# MY SOLUTION

def largest_pair_sum(numbers):
    return sum(sorted(numbers, reverse=True)[:2])


# DEMONSTRATION

print(largest_pair_sum([10, 14, 2, 23, 19]))
print(largest_pair_sum([-100, -29, -24, -19, 19]))
print(largest_pair_sum([1, 2, 3, 4, 6, -1, 2]))
print(largest_pair_sum([-10, -8, -16, -18, -19]))
