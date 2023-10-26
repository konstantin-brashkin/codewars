# Find the total sum of internal angles (in degrees) in an n-sided simple polygon.
# N will be greater than 2.

def angle(n):
    return 180 * (n - 2)


print(angle(3))
print(angle(4))
print(angle(5))
print(angle(25))
