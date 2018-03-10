# 9. Special Pythagorean triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from _timeit import timeit

@timeit
def FindTripletA(num):
    squares = []
    for i in range(num - 1):
        squares.append(i**2)
    for a in range(1, num - 2):
        for b in range(a + 1, num - a - 1):
            c = 1000 - (a + b)
            if squares[c] == (squares[a] + squares[b]):
                print (a, b, c)
                return a * b * c

@timeit
def FindTripletB(num):
    for a in range(1, num - 2):
        for b in range(a + 1, num - a - 1):
            c = 1000 - (a + b)
            if c**2 == a**2 + b**2:
                return a * b * c


print(FindTripletA(1000))
print(FindTripletB(1000))