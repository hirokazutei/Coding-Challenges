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
                return a * b * c

# Solution C
@timeit
def FindTripletC(num):
    num_limit = int(num//2)
    for a in range(1, num_limit - 1):
        for b in range(a + 1, num - a):
            if 500000 == 1000 * (a + b) - a * b:
                c = 1000 - (a + b)
                return a * b * c


# Optimal Solution
@timeit
def FindTripletD(num):
    num_half = num//2
    min_limit = int((num_half)**1/2 -1)
    if min_limit % 1 != 0:
        min_limit = int(min_limit + 1)
    for m in range(2, min_limit):
        if num_half % m == 0:
            sm = num_half // m
            while sm % 2 == 0:
                sm = sm//2
            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1
            while k < 2 * m and k <= sm:
                if sm % k == 0 and CommonDenomenator(k,m):
                    d = num_half // (k * m)
                    n = k - m
                    a = d * (m * m - n * n)
                    b = 2 * d * m * n
                    c = d * (m * m + n * n)
                    return (a * b * c)
                k += 2

def CommonDenomenator(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return False
    else:
        a_limit = a**(1/2)
        b_limit = b**(1/2)
        n = 3
        while n <= a_limit and n <= b_limit:
            if a % n == 0 and b % n == 0:
                return False
            n+=2
    return True

"""
The Pythagoras triad can also be represented by: 
a = m**2 - n**2,  b = 2 * m * n,  c = m**2 + n**2
m > n > 0

Given this information and the fact that the primitive numbers' greatest common denominator is 1,
one can deduce the optimal solution, which is many magnitudes faster than the other solutions.
"""

print(FindTripletA(1000))
print(FindTripletB(1000))
print(FindTripletC(1000))
print(FindTripletD(1000))
