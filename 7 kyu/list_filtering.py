# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new
# list with the strings filtered out.


# MY SOLUTION

def filter_list(l):
    final_lst = []
    for element in l:
        if isinstance(element, int):
            final_lst.append(element)
    return final_lst


# DEMONSTRATION

print(filter_list([1, 2, 'a', 'b']))
