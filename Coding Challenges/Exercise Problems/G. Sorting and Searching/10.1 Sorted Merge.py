# 10.1 Sorted Merge
"""
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order.
"""

import random


def createArray(number):
    array = []
    a = 0
    for i in range(number):
        a = random.randint(a, a + 10)
        array.append(a)

    return array

def crawlInsert(item, A, position):
    for num in range(position, len(A)):
        if item <= A[0]:
            A.insert(num, item)
            break
        elif item >= A[-1]:
            A.insert(num, item)
            break
        elif item >= A[num] and item <= A[num + 1]:
            A.insert(num + 1, item)
            break
    return num + 1

def merge(A, B):
    position = 0
    for item in B:
        position = crawlInsert(item, A, position)


A = createArray(10)
print(A)
B = createArray(10)
print(B)

merge(A, B)
print(A)