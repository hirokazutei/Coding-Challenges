# 23. Non-Abundant Sums
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written
as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though
it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# Brainstorm
"""
Sieve Addition: [O(N**2)]
We can use a sieve to find which numbers up to 28123 are abundant. We can then add up the combinations of abundant
numbers to cross off any numbers that CAN be derived from adding abundant numbers.
We can then sum up the non-abundant numbers.

Sieve Subtraction: [O(N * A) where A is the average iterations until we can determine if the number can be summed by two abundant numbers.]
Similarly, we can use a sieve to find which numbers up to 28123 are abundant. Then for each number, we can subtract
numbers lower than itself to see if there is a matching abundant number.
We can then sum up the non-abundant numbers.
"""

from _timeit import timeit

# Solution A
@timeit
def SumAbundant(num):
    sieve = [1 for i in range(num+1)]
    abundants = [0 for i in range(num+1)]
    abundant_sum = [0 for i in range(num+1)]
    total = 0
    for i in range(2, int(num//2)):
        a = i
        while a <= num:
            if i != a:
                sieve[a] += i #Does not count itself as a factor
            a += i
    for i in range(12, num+1):
        if i < sieve[i]:
            abundants[i] = sieve[i]
    for i in range(12, (num + 1)//2):
        if abundants[i] != 0:
            for j in range(12, num + 1 - i):
                if abundants[j] != 0:
                    abundant_sum[i+j] = 1
    for i in range(num+1):
        if abundant_sum[i] == 0:
            total += i
    return total


print(SumAbundant(28123))