# There are no explanations. You have to create the code that gives the following results in Python, Ruby, and Haskell:
#
# one_two_three(0) == [0, 0]
# one_two_three(1) == [1, 1]
# one_two_three(2) == [2, 11]
# one_two_three(3) == [3, 111]
# one_two_three(19) == [991, 1111111111111111111]
# And it should give the following results in Javascript, Scala, D, Go, and Rust:
#
# oneTwoThree(0) == ['0', '0']
# oneTwoThree(1) == ['1', '1']
# oneTwoThree(3) == ['3', '111']
# oneTwoThree(19) == ['991', '1111111111111111111']
# In C, the results are to be assigned to seperate pointers.


def one_two_three(n):
    sequence = 0 if n == 0 else int("1" * n)
    if n <= 9:
        return [n, sequence]
    else:
        last_number = n % 9
        digit = "9" * (n // 9)
        digit += str(last_number) if last_number > 0 else ''
        return [int(digit), sequence]


print(one_two_three(3))
print(one_two_three(19))
print(one_two_three(0))
print(one_two_three(171))
