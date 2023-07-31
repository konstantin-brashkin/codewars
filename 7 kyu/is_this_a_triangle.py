# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built
# with the sides of given length and false in any other case.
#
# (In this case, all triangles must have surface greater than 0 to be accepted).

# MY SOLUTION

def is_triangle(a, b, c):
    if a and b and c <= 0:
        return False
    else:
        if (a + b > c) and (a + c > b) and (b + c > a):
            return True
        else:
            return False


# DEMONSTRATION

print(is_triangle(3, 3, -1))
print(is_triangle(7, 2, 2))
print(is_triangle(1, 2, 2))

