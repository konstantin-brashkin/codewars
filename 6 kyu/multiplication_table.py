# Your task, is to create N×N multiplication table, of size provided in parameter.
#
# For example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:
#
# [[1,2,3],[2,4,6],[3,6,9]]


# MY SOLUTION

def multiplication_table(size):
    if size == 1:
        return [[1]]
    elif size > 1:
        first_arr = [i for i in range(1, size + 1)]
        final_arr = [first_arr]

        counter = 1
        while counter != size:
            new_arr = []
            counter_index = 0
            for element in final_arr[-1]:
                new_arr.append(element + first_arr[counter_index])
                counter_index += 1
            final_arr.append(new_arr)
            counter += 1

        return final_arr


# DEMONSTRATION

print(multiplication_table(1))
print(multiplication_table(3))
print(multiplication_table(4))
print(multiplication_table(5))
