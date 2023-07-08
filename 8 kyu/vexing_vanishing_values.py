# Confusion, perplexity, a mild headache. These are just a sample of the things you have experienced in the last few
# minutes while trying to figure out what is going on in your code.
#
# The task is very simple: accept a list of values, and another value n, then return a new list with every value
# multiplied by n. For example, [1, 2, 3] and 4 should result in [4, 8, 12].


# MY SOLUTION


def mul_by_n(lst, n):
    final_list = []
    for x in lst:
        current_value = x * n
        final_list.append(current_value)
    return final_list


# DEMONSTRATION

print(mul_by_n([1, 2, 3], 4))


