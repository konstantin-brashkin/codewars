# Complete the solution so that the function will break up camel casing, using a space between words.
# #
# # Example
# # "camelCasing"  =>  "camel Casing"
# # "identifier"   =>  "identifier"
# # ""             =>  ""


# MY SOLUTION

def solution(s):
    final_str = ''
    for element in s:
        if not element.isupper():
            final_str += element
        elif element.isupper():
            final_str += f" {element}"
    return final_str


# DEMONSTRATION

print(solution("breakCamelCase"))
print(solution("helloWorld"))
print(solution("brakence"))
print(solution(""))
