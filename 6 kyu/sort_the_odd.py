# Task You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the
# even numbers at their original positions.
#
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# MY SOLUTION

def sort_array(source_array):
    odd_numbers = []
    final_list = []

    for element in source_array:
        if element % 2 != 0:
            odd_numbers.append(element)
    sorted_odds = sorted(odd_numbers, reverse = True)

    for element in source_array:
        if element % 2 != 0:
            final_list.append(sorted_odds[-1])
            del sorted_odds[-1]
        else:
            final_list.append(element)
    return final_list


# DEMONSTRATION

print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([5, 3, 2, 8, 1, 4]))
