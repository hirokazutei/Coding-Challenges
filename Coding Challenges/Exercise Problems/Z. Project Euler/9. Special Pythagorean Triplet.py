# 9. Special Pythagorean triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from _timeit import timeit

# Brainstorm
"""
Pure Brute Force:
The brute force method is to simply iterate though every possible combinations of a, b and c to find the three variables that
meets the specific condition. Without any optimization, it would mean that it would require O(N**3) steps.

Small Optimization:
One obvious optimization is to derive c from a and b. Since they all must add up to 1000, it would mean that c is
known once we decide a and b.

More Optimization:
Since a + b + c = 1000 and a**2 + b**2 = c**2:
this means that c = 1000 - a - b, we can replace the c**2 in the previous equation with (1000 - a - b)**2
a**2 + b**2 = (1000 - a + b)**2
a**2 + b**2 = 1000000 - 2000a - 2000b + a**2 + 2ab + b**2
Eliminate common values on both sides and shift the 1000000 to the left, simplify it...
500000 = 1000(a + b) - a * b
We can use this formula to find which numbers are a and b.
"""

# Solution A
@timeit
def FindTripletA(num):
    for a in range(1, num - 2):
        for b in range(a + 1, num - a - 1):
            c = 1000 - (a + b)
            if c**2 == a**2 + b**2:
                return a * b * c

# Solution B
@timeit
def FindTripletB(num):
    squares = []
    num_limit = int(num) #This can be made faster
    for i in range(num):
        squares.append(i**2)
    for a in range(1, num_limit - 1):
        for b in range(a + 1, num_limit - a):
            c = 1000 - (a + b)
            if squares[c] == (squares[a] + squares[b]):
                print (a, b, c)
                return a * b * c

# Optimal solution
@timeit
def FindTripletC(num):
    num_limit = int(num//2)
    for a in range(1, num_limit - 1):
        for b in range(a + 1, num - a):
            if 500000 == 1000 * (a + b) - a * b:
                c = 1000 - (a + b)
                return a * b * c

print(FindTripletA(1000))
print(FindTripletB(1000))
print(FindTripletC(1000))
