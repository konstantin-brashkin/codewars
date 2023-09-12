# Scenario
# Several people are standing in a row divided into two teams.
# The first person goes into team 1, the second goes into team 2, the third goes into team 1, and so on.
#
# Task Given an array of positive integers (the weights of the people), return a new array/tuple of two integers,
# where the first one is the total weight of team 1, and the second one is the total weight of team 2.
#
# Notes
# Array size is at least 1.
# All numbers will be positive.
# Input >> Output Examples
# rowWeights([13, 27, 49])  ==>  return (62, 27)


# MY SOLUTION

def row_weights(array):
    first_weight = sum(array[i] for i in range(len(array)) if i % 2 == 0)
    second_weight = sum(array[i] for i in range(len(array)) if i % 2 != 0)
    return first_weight, second_weight


# DEMONSTRATION

print(row_weights([50, 60, 70, 80]))
print(row_weights([70, 58, 75, 34, 91]))
print(row_weights([29, 83, 67, 53, 19, 28, 96]))
print(row_weights([39, 84, 74, 18, 59, 72, 35, 61]))
