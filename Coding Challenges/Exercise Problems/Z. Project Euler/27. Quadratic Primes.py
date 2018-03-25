# 27. Quadratic Primes

"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However,
when n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41 is divisible by 41, and certainly
when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n=0.
"""

# Brainstorm
"""
Brute Force:
The brute force method would be check every combination of n^2 + an + b, and check if for each n from 0, if the 
resulting number is a prime. Very time-consuming process.

Optimized:
Since we are checking for primes, it is helpful to construct a prime checker using a sieve.
The largest prime check possible would be for when n = 1000, a = 999, b = 1000 since the equation can be reduced to:
= 1000 * 1000 + 1000 * 999 + 1000
= 1000 * 2000

Since we start from n = 0, when n is 0, since it is being multiplied to a, the resultant number will be b.
Thus, b can only be primes, which reduces many options.

We begin collecting possibilities with n = 1, thus append all possibilities of:
= 1 * 1 + 1 * a + b
= 1 + a + b
where the resultant number is a prime. We have reduced the possibilities from 1,000,000 checks in brute force to
effectively only around 100,000 possibilities.

Finally, we iterate through n from 2 and onwards, reducing the amount of possibilities where the resultant
number becomes a non-prime number, ending up with one final pair of number with the longest chain of primes.

The time complexity of checking around 100,000 possibilities is not very high since after 1 iteration, the possibilities
gets reduced to less than 40,000, and then quickly to less than 10,000 afer 3 iterations.
"""
from _timeit import timeit

# Solution A
@timeit
def QuadraticPrimesA(num):
    largest_prime = (((num) ** 2) * 2 + num)//100
    primes = [0] * largest_prime
    limit = len(primes)//2
    i = 2
    while i <= limit: # Create a sieve to determine all primes
        a = i * 2
        while a < len(primes):
            primes[a] = 1
            a += i
        i += 1
        while primes[i] != 0:
            i += 1
            if i > limit:
                break
    even = 1 if num % 2 == 0 else 0
    b_option = [b for b in range(-num - even, num + even, 2) if primes[abs(b)] == 0] # B has to be a prime because b is the result when n = 0
    possible = [[a, b] for a in range(-num, num) for b in b_option if primes[abs(1 + a + b)] == 0]
    n = 2
    while len(possible) > 1:
        for comb in range(len(possible) - 1, -1, -1):
            result = abs(n * n + n * possible[comb][0] + possible[comb][1])
            if primes[result] == 1:
                possible.pop(comb)
        n += 1
    return possible[0][0] * possible[0][1]

print(QuadraticPrimesA(1000))