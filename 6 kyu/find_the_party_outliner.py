# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The
# array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer
# N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)


# MY SOLUTION

def find_outlier(integers):
    counter_odd = 0
    counter_even = 0
    for number in integers:
        if number % 2 == 0:
            counter_even += 1
        else:
            counter_odd += 1
    for number in integers:
        if (counter_even < counter_odd) and (number % 2 == 0):
            return number
        elif (counter_even > counter_odd) and (number % 2 != 0):
            return number


# DEMONSTRATION

print(find_outlier([2, 4, 6, 8, 10, 3]))
