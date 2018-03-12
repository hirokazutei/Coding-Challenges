# 10. Summation of Primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# Brainstorm
"""
Brute Force:
The brute force method is to check every number and divide it by every number until itself to see if it is evenly divisible.
If not, that number is a prime and can be summed until we reach over 2,000,000.

Optimizations:
The first thing to do is that to check if a prime candidate is prime, it only needs to be divided by the primes until the 
squareroot of the candidate. In addition, since prime candidates after 2 and 3 can be represented as 6k + / - 1, 
we can only check if 6k + / - 1 is a prime until 2,000,000.
"""
from _timeit import timeit

#Solution A
@timeit
def SumPrimesA(limit):
    sum = 5
    cur_num = 6
    track_prime = [3]
    while cur_num < limit:
        if (IsPrime(cur_num - 1, track_prime)):
            if cur_num - 1 < limit**1/2:
                track_prime.append(cur_num - 1)
            sum += cur_num - 1
        if (IsPrime(cur_num + 1, track_prime)):
            if cur_num + 1 < limit**1/2:
                track_prime.append(cur_num + 1)
            sum += cur_num + 1
        cur_num += 6
    return sum

def IsPrime(candidate, primes):
    sqrt = candidate**(1/2)
    for item in primes:
        if candidate % item == 0:
            return False
        elif item > sqrt:
            return True
    return True


# Optimal Solution
@timeit
def SumPrimesB(limit):
    bound = (limit - 1)//2
    crosslimit = int(limit**(1/2)-1)//2
    sieve = [False] * bound
    sieve[0] = True
    for n in range(1, crosslimit):
        if not sieve[n]:
            for m in range(2*n*(n+1), bound, 2*n+1):
                sieve[m] = True
    sum = 2
    for i in range(len(sieve)):
        if not sieve[i]:
            sum += i * 2 + 1
    return sum


# Optimal Solution Explanation
"""
The optimal solution is to use a sieve. Make a binary array from 0 to 2,000,000, setting all values as true.
Begin with 2, and set all indexes that are multiples of 2 to false. Iterate through sieve to discover the next value
that is still true, that will be the next prime, 3. Repeat the process where the multiple of the primes are turned to false.
Do this until the square root of 2,000,000, and the resultant indexes with true are all the primes.
This procedure takes N(A*B) where A is the number of primes below square root of 2,000,000 and B is the average times a
prime can fit into 2,000,000.

This can be optimized further by taking into consideration that multiples of 2 are always non-primes. Meaning that we
can reduce the array size down to half.
"""

print(SumPrimesA(2000000))
print(SumPrimesB(2000000))