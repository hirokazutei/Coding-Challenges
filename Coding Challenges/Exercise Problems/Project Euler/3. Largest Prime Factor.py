# 3. Largest Prime Factor

"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

# Brain Storm
"""
The brute force approach is to divide the number by 2 to to the square root of itself and see if there are any remainder.
If there is no remainder, check if the complimentary multiple is a prime or not.
Since if the number is not divisible by 2, it would mean that it cannot be divisible by any even number,
We can cut the process time by avoiding dividing by multiples of 2.
We can do the same with 3, 5, 7 and other factors. 
"""

# Solution 1 & Optimal Solution
def LargestPrime(num):
    largest = 0
    if num % 2 is 0:
        if IsPrime(num/2):
            return num/2
        else:
            largest = 2
    for i in range(3, int(num**(1/2)), 2):
        if num % i == 0:
            j = num/i
            if IsPrime(j) and j > largest:
                return j
            if i > largest and IsPrime(i):
                largest = i
    return largest

def IsPrime(num):
    for i in range(2, int(num**(1/2))):
        if num % i == 0:
            return False
    return True

# Optimal Solution Explanation
"""
Turns out, this is the best approach, according to Project Euler.
Process time of O(A * B) where A is square root of the input divided by 2 and B is the average increments
needed to discover if the number is a prime factor or not.
"""

print(LargestPrime(600851475143))
