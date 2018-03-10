# 1. Multiple of 3 and 5
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# Brainstorm
"""
Brute Force:
The most obvious brute force solution is to increment through every number between 3 to 1000 and check if each number
can be divided by 3 or 5, producing a process time of O(N) where N is the range.

Multiple:
Another method is to compute products of 3 until it reaches beyond the range, adding up all the numbers.
Then compute products of 5, making sure that they are indivisible by 3 (since we have computed 3 already) and 
sum up the numbers until the multiples of 5 becomes larger or equal to 1000. This will result a process time of
O(N/a + N/b) where a and b are the multiples.

A smarter way to check if the product of 5 is also a multiple of 3 by keeping track of iterations of products of 5.
Meaning that the product of 5 becomes divisible by 3 every 3 steps. This will reduce the computational power
greatly since it avoids the division process, which is typically quite processor heavy.
"""

# Solution A
class MultipleTracker:
    def __init__(self, multipleA, multipleB, range):
        self.multipleA = multipleA
        self.multipleB = multipleB
        self.range = range
        self.sum = 0

    def MultipleA(self):
        self.sum = 0
        product = self.multipleA
        while product < self.range:
            self.sum += product
            product += self.multipleA
        count = 0
        product = self.multipleB
        print(self.multipleA)
        while product < self.range:
            count += 1
            if count is self.multipleA:
                count = 0
                product += self.multipleB
            else:
                self.sum += product
                product += self.multipleB
        return self.sum

# Optimal Solution
    def MultipleB(self):
        self.sum = 0
        self.sum += self.SumMul(self.multipleA, self.range)
        self.sum += self.SumMul(self.multipleB, self.range)
        self.sum -= self.SumMul(self.multipleA * self.multipleB, self.range)
        return self.sum

    def SumMul(self, multiple, range):
        largest = (range - 1)//multiple
        if (largest % 10) % 2 is 0:
            return int(multiple * ((1 + largest) * largest/2))
        else:
            return int(multiple * ((1 + largest) * (largest//2 + 0.5)))

# Optimal Solution Explanation
"""
The solution on Project Euler is to treat the problem as the following function:
Sum = (A * ∑(1 to range//A)) + (B +  ∑(1 to range//B)) - ((A * B) +  ∑(1 to range//(A + B)))
This is a beautiful solution for regardless of the range of the problem, it can be solved in N(1).
I had thought about this method, however, for some reason, I had dismissed it because I was adamant about
solving this problem with no multiplication or division, thinking that it would save processing time.
"""


track = MultipleTracker(3, 5, 1000)
print(track.MultipleA())
print(track.MultipleB())
