# Number Spiral Diagonals

"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

# Brainstorm
"""
Simple Solution:
Each layer expands by 2 and the 4 numers increase by the layer size - 1.
The next layer's first number is the last number + new layer size - 1.
We can iterate through until the layer reaches the desired limit.

Optimized:
We can simplify the previous function by grouping each layer's average by adding (layer * 4 + 1) to the previous average,
staring from 1.
average_1 = 1
average_2 = 6
average_3 = 27
etc.
And add that number 4 times to the total until the layer reaches the limit.
"""

from _timeit import timeit

# Solution A
@timeit
def NumberSpiralDiagonalsA(num):
    curnum, layer, total = 1, 1, 1
    while layer < num:
        layer += 2
        curnum += layer - 1
        total += curnum
        for i in range(3):
            curnum += layer - 1
            total += curnum
    return total


# Solution B
@timeit
def NumberSpiralDiagonalsB(num):
    curnum, layer, total = 1, 1, 1
    while layer < num:
        curnum += (layer * 4 + 1)
        total += curnum * 4
        layer += 2
    return total

print(NumberSpiralDiagonalsA(1001))
print(NumberSpiralDiagonalsB(1001))
