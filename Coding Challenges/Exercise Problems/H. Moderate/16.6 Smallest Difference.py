# 16.6 Smallest Difference
"""
Given two arrays of integers, compute the pairs of values (one value in each array) with the smallest (non-negative).
Return the difference
"""

lookUp = [''] * 1000
import random

#O(N + A + B) where N is the maximum value


def lookUp(arrayA, arrayB):
    maxA = max(arrayA)
    maxB = max(arrayB)
    if maxA >= maxB:
        lookUp = [''] * (maxA + 1)
    else:
        lookUp = [''] * (maxB + 1)
    for item in arrayA:
        lookUp[item] = 'a'
    for item in arrayB:
        if lookUp[item] is 'a':
            return "{} difference. Pair is: {} & {}".format(0, item, item)
        else:
            lookUp[item] = 'b'
    char = None
    diff = len(lookUp)
    posA = None
    posB = None
    for item in range(len(lookUp)):
        if lookUp[item] is 'a' or lookUp[item] is 'b':
            if char is None:
                position = item
                char = lookUp[item]
            elif char is not lookUp[item]:
                char = lookUp[item]
                difference = item - position
                if difference < diff:
                    diff = difference
                    if char is 'a':
                        posB = position
                        posA = item
                    else:
                        posA = position
                        posB = item
                position = item
            elif char is  lookUp[item]:
                potision = item
    return "{} difference. Pair is: {} & {}".format(diff, posA, posB)

def generateNum(num):
    array = []
    for i in range(num):
        array.append(random.randint(0, 10000))
    return array

arrayA = generateNum(50)
arrayB = generateNum(50)
print(lookUp(arrayA, arrayB))