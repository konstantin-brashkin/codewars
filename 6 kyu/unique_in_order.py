# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]


# MY SOLUTION


def unique_in_order(sequence):
    final_list = []
    if len(sequence) > 0:
        final_list = [sequence[0]]
    else:
        return final_list

    for element in sequence:
        if final_list[-1] != element:
            final_list.append(element)

    return final_list


# DEMONSTRATION

print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
