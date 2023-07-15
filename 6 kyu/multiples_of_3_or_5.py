# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
#
# Note: If the number is a multiple of both 3 and 5, only count it once.


# MY SOLUTION

def solution(number):
    digits = [i for i in range(0, number)]
    final_int = 0
    for element in digits:
        if (element % 3 == 0) or (element % 5 == 0):
            final_int += element

    return final_int


# DEMONSTRATION

print(solution(4))
print(solution(6))
