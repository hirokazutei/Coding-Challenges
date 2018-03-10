# 10. Summation of Primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


# Brainstorm
"""
Since prime candidates after 2 and 3 can be represented as 6k + / - 1, instead of finding all the primes, it may be
faster to sum all possible prime candidates and subtract non-primes from the candidates until the given limit
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


print(SumPrimesA(2000000))
print(SumPrimesB(2000000))


# Optimal Solution Explanation
"""
Prime candidates above 2 and 3 can actually be narrowed down to the formula 6k -/+ 1.
For this reason, instead of incrementing 2 to find the potential candidate, one can simply increment k
and see if the two possible outcomes end up as primes.
As testing shows, solution A is approx. 5 times slower than B, and B is almost twice as slow as C.
"""