# Task Given a list of digits, return the smallest number that could be formed from these digits, using the digits
# only once (ignore duplicates).
#
# Notes:
# Only positive integers will be passed to the function (> 0 ), no negatives or zeros.
# Input >> Output Examples
# minValue ({1, 3, 1})  ==> return (13)
# Explanation:
# (13) is the minimum number could be formed from {1, 3, 1} , Without duplications


# MY SOLUTION

def min_value(digits):
    return int(''.join(sorted(map(str, set(digits)))))


# DEMONSTRATION

print(min_value([1, 3, 1]))
print(min_value([4, 7, 5, 7]))
print(min_value([4, 8, 1, 4]))
