# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a
# var = parameter.Recall
# that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is
# non-negative.
#
# Examples:(Input --> Output)
#
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square


# MY SOLUTION

import math


def find_next_square(sq):
    square = math.sqrt(sq)
    if square.is_integer():
        new_square = square + 1
        while not new_square.is_integer():
            new_square += 1
        return int(new_square ** 2)
    else:
        return -1


# DEMONSTRATION

print(find_next_square(121))
print(find_next_square(131))
