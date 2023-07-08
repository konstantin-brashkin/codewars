# You get an array of numbers, return the sum of all of the positives ones.
#
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
#
# Note: if there is nothing to sum, the sum is default to 0.


# MY SOLUTION

def positive_sum(arr):
    sum_positive = 0
    for number in arr:
        if number >= 0:
            sum_positive += number
    return sum_positive


# DEMONSTRATION

print(positive_sum([1,-2,3,4,5]))
