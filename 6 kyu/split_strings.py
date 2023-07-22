# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd
# number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


# MY SOLUTION

def solution(s):
    final_str = []
    for i in range(0, len(s), 2):
        final_str.append(s[i:i + 2])

    try:
        if len(final_str[-1]) == 1:
            final_str[-1] += "_"
    except IndexError:
        pass

    return final_str


# DEMONSTRATION

print(solution(""))
print(solution("asdfadsf"))
print(solution("asdfads"))
