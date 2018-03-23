# 24. Lexicographic permutations

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

# Brainstorm
"""
Bruteforcing would be incredibly inefficient in terms of time complexity.

Since we know that the number of possible permutation of 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is 10!, we know that
the last lexicographic permutation would be 9876543210 and it would be the 3628800th permutation.

Consequently, the (9!)th permutation would be 0987654321 since 987654321 is the permutation of the previous example
without the 0 and (9!+1)th permutation would be 1987654320. Which means that (9!n + 1)th permutation starts with n-th number.

From the number given (1,000,000 this case) we can see how many times each m! fits into it from 9 to 0 and resultant
n would help us find the n-th remaining number.

Lexicographic permutation of 0, 1, 2, 3 are:
0123        1023        2013        3012
0132        1032        2031        3021
0213        1203        2103        3102
0231        1230        2130        3120
0312        1302        2301        3201
0321        1320        2310        3210
n = 0       n = 1       n = 2       n = 3
"""

def LexicographicPermutation(num, digits):
    max = 1
    final_index = []
    num -= 1
    if type(digits) is int:
        numbers = []
        num_count = digits + 1
        for i in range(num_count):
            max *= (i + 1)
            numbers.append(i)
    elif type(digits) is list:
        digits.sort()
        numbers = digits
        num_count = len(digits)
        for i in range(num_count):
            max *= (i + 1)
            numbers.append(i)
    if max < num:
        return False
    for i in range(num_count, 0, -1):
        max /= i
        fit = int(num // max)
        num -= max*fit
        final_index.append(numbers[fit])
        numbers.pop(fit)
    return final_index

print(LexicographicPermutation(1000000, [0,1,2,3,4,5,6,7,8,9]))