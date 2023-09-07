# You will be given an array and a limit value. You must check that all values in the array are below or equal to the
# limit value. If they are, return true. Else, return false.
#
# You can assume all values in the array are numbers.


# MY SOLUTION

def small_enough(array, limit):
    return True if (max(array) <= limit) else False


# DEMONSTRATION

print(small_enough([66, 101], 200))
print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100))
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115], 120))
