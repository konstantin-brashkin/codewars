# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
# elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


# MY SOLUTION

def move_zeros(lst):
    zeros = []
    others = []
    for element in lst:
        if element == 0:
            zeros.append(element)
        else:
            others.append(element)
    return others + zeros


# DEMONSTRATION

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
