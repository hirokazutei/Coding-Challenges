# 6. Sum Square Difference
"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


# Brainstorm
"""
The brute force method is to simply compute the sum of squares and the squares of the sum and subtract to get the difference.
However, there should be a much more computationally light way to do this:
Take a small example of 1 to 4.

SumSq = 1^2 + 2^2 + 3^2 + 4^2
SqSum = (1 + 2 + 3 + 4)^2

Which the latter can be expanded to be:

SqSum = 1x1 + 1x2 + 1x3 + 1x4 + 2x1 + 2x2 + 2x3 + 2x4 + 3x1 + 3x2 + 3x3 + 3x4 + 4x1 + 4x2 + 4x3 + 4x4
SqSum = (1^1 + 2^2 + 3^2 + 4^2) + (1x2 + 1x3 + 1x4 + 2x1 + 2x3 + 2x4 + 3x1 + 3x2 + 3x4 + 4x1 + 4x2 + 4x3)
SqSum = SumSq + Difference

Notice how SumSq exists as a part of SqSum. Thus, if we find a way to efficiently compute the difference, we can find the answer.
The equation can be simplified further...

Difference = 2(1x2) + 2(1x3) + 2(1x4) + 2(2x3) + 2(2x4) + 2(3x4)
Difference = 2(1x2 + 1x3 + 1x4 + 2x3 + 2x4 + 3x4)
Difference = 2(1(2 + 3 + 4) + 2(3 + 4) + 3(4))

Difference = 2(14, 12, 9, 4)

Following this pattern, we can simply multiply each number from min to max - 1 with the sum of numbers more than it self,
then multiply the final result by 2 to obtain the answer.
The sum function does not have to be repeated since the resultant can simply subtract itself.
"""

# Solution A
def SumSquareDifferenceA(min, max):
    sum = int((min + max) * ((max - min + 1) / 2))
    total = 0
    for i in range(min, max+1):
        sum -= i
        total += sum * i
    return total * 2

# Optimal Solution
def SumSquareDifferenceB(limit):
    sum = limit * (limit + 1)/2
    sum_sq = (2 * limit + 1) * (limit + 1) * limit / 6
    return (sum**2 - sum_sq)

# Optimal Solution Explanation
"""
Turns out that there was a function to compute the sum of squares!
But since there is, this problem can always be solved by N(1).
This is a great piece of knowledge to have!
"""

print(SumSquareDifferenceA(1, 1000))
print(SumSquareDifferenceB(1000))