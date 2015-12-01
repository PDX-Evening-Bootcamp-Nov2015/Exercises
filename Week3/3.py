# Make function that takes a number and returns a two-dimensional array (i.e. a list of lists) or random
# numbers that are between 1 and n squared.  N should determine the size of the array and the limit on random.
# Example: make_2d(3) should return [[n, n2, n3], [n4, n5, n6], [n7, n8, n9]] where any n is 1 <= n <= 9 (3 squared)
import random

def dem_2(n):
    outer = []
    for x in range(n):
        inner = []
        for y in range(n):
            inner.append(random.randint(1, n**2))
        outer.append(inner)
    return outer

print(dem_2(3))
