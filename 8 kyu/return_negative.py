# In this simple assignment you are given a number and have to make it negative. But maybe the number is already
# negative?


# MY SOLUTION

def make_negative(number):
    if number >= 0:
        return number * -1
    else:
        return number

# DEMONSTRATION


print(make_negative(42))
print(make_negative(-3))
