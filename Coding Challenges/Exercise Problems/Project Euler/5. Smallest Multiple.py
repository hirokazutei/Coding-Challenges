# 5. Smallest Multiple
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math

# Brain Storm
"""
Instantly, two rules comes up in mind:
1. The value has to be able to be divided by prime numbers and prime numbers are not evenly divisible by anything but itself...
    This means that the final number will be a product of at least all the prime numbers.
2. If the final number can be divided by a number that has its own factors, then it can be divided by its factors too.
    This means that if we make the final number with the products that includes 6, 3 and 2 will not need to be included.

Thus the issue becomes: what products to choose to multiply them all together to construct the smallest multiple?
    A. We can iterate through the largest numbers, find their factors (or lack thereof) and simply keep a list of numbers
    until every number in the range is found. 
    B. Since all numbers with factors have a prime or a power of the prime, we can simply add primes and their powers
    as long as it is smaller than the range.
"""

# Solution A
def SmallestMultipleA(min, max):
    if min <= 1:
        min = 2
    product = 1
    value_store = []
    multiply_values = []
    for i in range(min, max + 1):
        value_store.append([i, 0])
    for factor in range(max, min - 1, -1):
        append_it = True
        prime = True
        square = False
        for sub_factor in range(min, int(factor**(1/2)) + 1):
            if factor % sub_factor is 0:
                if sub_factor is factor//sub_factor:
                    value_store[sub_factor - min][1] = 1
                    square = True
                elif value_store[sub_factor - min][1] is 0 and value_store[factor//sub_factor - min][1] is 0:
                    value_store[sub_factor - min][1] = 1
                    value_store[factor//sub_factor - min][1] = 1
                    prime = False
                else:
                    append_it = False
                    prime = False
        if append_it or prime:
            if value_store[factor - min][1] is 0:
                multiply_values.append(factor)
                square = False
        if square and prime:
            multiply_values.append(factor)
    for items in multiply_values:
        product *= items
    print(multiply_values)
    return product

# Solution B & Optimal Solution
def SmallestMultipleB(min, max):
    if min <= 1:
        min = 2
    product = 1
    multiply_values = []
    for multiple in range(min, max):
        prime = True
        for factors in range(min, int(multiple**(1/2)) + 1): # Can be replaced with a list of factors
            if multiple % factors is 0:
                prime = False
                break
        if prime:
            i = math.floor(math.log(max, multiple))
            multiply_values.append(multiple**(i))
            """ # Method that does not use the math library
            i = 1
            while multiple**i <= max:
                i += 1
            multiply_values.append(multiple**(i-1))
            """
    for items in multiply_values:
        product *= items
    print(multiply_values)
    return product

# Optimal Solution Explanation
"""
The explanation given on Project Euler is the same as Solution 2. 
"""

print(SmallestMultipleA(1, 20))
print(SmallestMultipleB(1, 20))