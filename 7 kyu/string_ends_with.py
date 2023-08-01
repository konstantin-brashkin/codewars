# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (
# also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


# MY SOLUTION

def solution(text, ending):
    return text.endswith(ending)

# DEMONSTRATION


print(solution("samurai", "ai"))


