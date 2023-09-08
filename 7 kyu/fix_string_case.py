# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to
# convert that string to either lowercase only or uppercase only based on:
#
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
# For example:
#
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.


# MY SOLUTION

def solve(s):
    counter_lower = 0
    counter_upper = 0
    for i in s:
        if i.islower():
            counter_lower += 1
        else:
            counter_upper += 1
    return s.lower() if counter_lower >= counter_upper else s.upper()


# DEMONSTRATION

print(solve("code"))
print(solve("CODe"))
print(solve("COde"))
