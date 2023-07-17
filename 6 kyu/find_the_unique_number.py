# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.

# MY SOLUTION

def find_uniq(arr):
    unique_elements = list(set(arr))
    for element in unique_elements:
        if (element != arr[0]) or (element != arr[1]):
            return element


# DEMONSTRATION

print(find_uniq([3, 10, 3, 3, 3]))
