# 7. 10001st Prime

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# Brainstorm
"""
The brute force method is to simply iterate through numbers, divide by numbers from 2 to square root of itself, then 
if none of the potential factors can divide the number evenly, deem it as a prime. Repeat the process until 10001st
prime is found.

However, since primes are numbers indivisible by anything but by it self and one, for all subsequent numbers bigger 
than prime number P, we are assured that 2P, 3P... nP are not going to be primes.
Perhaps we can keep track of primes that we have encountered and count up to N, finding and keeping track of
primes by checking that they are not multiples of previous primes by incrementing a list of primes.

We speed up the process by incrementing by 2, since even numbers after 2 cannot be prime.
"""
from _timeit import timeit

# Solution A
@timeit
def FindNthPrimeA(N):
    track_prime = [[3, 3]]
    primenum = 1
    number = 3
    tracking = 0
    trackmul = 9
    if N == 1:
        return 2
    while primenum != N - 1:
        number += 2
        is_prime = True
        for primes in range(tracking):
            track_prime[primes][0] -= 2
            if track_prime[primes][0] == 0:
                track_prime[primes][0] = track_prime[primes][1]
                is_prime = False
            elif track_prime[primes][0] == -1:
                track_prime[primes][0] = track_prime[primes][1]-1
        if trackmul == number:
            tracking += 1
            trackmul = track_prime[tracking][0]**2
        elif is_prime:
            track_prime.append([number, number])
            primenum += 1
    return number

# Solution B
@timeit
def FindNthPrimeB(N):
    track_prime = []
    primenum = 1
    number = 1
    if N == 1:
        return 2
    while primenum != N:
        number += 2
        is_prime = True
        sqrt = number**(1/2)
        for primes in range(len(track_prime)):
            if number % track_prime[primes] == 0:
                is_prime = False
                break
            if track_prime[primes] > sqrt:
                is_prime = True
                break
        if is_prime:
            track_prime.append(number)
            primenum += 1
    return number

# Optimal Solution
@timeit
def FindNthPrimeC(N):
    primenum = 2
    count = 0
    track_prime = []
    if N < 1:
        return False
    elif N <= 2:
        return N + 1
    while primenum < N:
        count += 1
        if (IsPrime(6 * count - 1, track_prime)):
            primenum += 1
            track_prime.append(6*count-1)
        if (IsPrime(6 * count + 1, track_prime)):
            primenum += 1
            track_prime.append(6*count+1)
    if primenum == N:
        return track_prime[-1]
    else:
        return track_prime[-2]

def IsPrime(candidate, primes):
    sqrt = candidate**(1/2)
    for item in primes:
        if candidate % item == 0:
            return False
        elif item > sqrt:
            return True
    return True

# Optimal Solution
"""
Prime candidates above 2 and 3 can actually be narrowed down to the formula 6k -/+ 1.
For this reason, instead of incrementing 2 to find the potential candidate, one can simply increment k
and see if the two possible outcomes end up as primes.
As testing shows, solution A is approx. 5 times slower than B, and B is almost twice as slow as C.
"""

#print(FindNthPrimeA(10001))
#print(FindNthPrimeB(10001))
print(FindNthPrimeC(10001))

