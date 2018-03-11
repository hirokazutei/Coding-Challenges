# 10.4 Sorted Search, No Size
"""
You are given an array-like data structure Listy which lacks a size method.
It does, however, have an elementAt(i) method that returns the element at index i in O(1) time.
If i is beyond the bounds of the data structure, it returns -1.
(For this reason, the data structure only supports positive integers.)
Given a Listy which contains sorted, positive integers, find the index at which element x occurs.
If x occurs multiple times, you may return any index.
"""
import random

#Do a binary search that hops to the n exponent of two to see if

def hopSearch(item, array, begin = None, end = None):
    if begin is None:
        begin = 0
        end = 2
    if elementAt(begin, array) is item:
        return begin
    elif elementAt(end, array) is -1:
        mid = begin + (end - begin)//2
        if elementAt(mid, array) is item:
            return mid
        elif elementAt(mid, array) < item:
            return hopSearch(item, array, mid + 1, end - 1)
        elif elementAt(mid, array) > item:
            return hopSearch(item, array, begin + 1, mid - 1)
    elif elementAt(end, array) is item:
        return end
    elif elementAt(begin, array) < item and elementAt(end, array) > item:
        return binarySearch(item, array, begin + 1, end - 1)
    else:
        return hopSearch(item, array, end + 1, end * 2)

def binarySearch(item, array, begin, end):
    mid = begin + (end - begin)//2
    if elementAt(begin, array) is item:
        return begin
    elif elementAt(end, array) is item:
        return end
    elif elementAt(mid, array) is item:
        return mid
    else:
        if elementAt(mid, array) > item:
            return binarySearch(item, array, begin + 1, mid - 1)
        elif elementAt(mid, array) < item:
            return binarySearch(item, array, mid + 1, end - 1)

def generateArray(num):
    array = []
    a = 0
    for numbers in range(num):
        a = random.randint(a, a + 3)
        array.append(a)
    b = array[random.randint(0, num - 1)]
    return array, b

def elementAt(i, array):
    if i >= len(array):
        return -1
    else:
        return array[i]

Listy, search = generateArray(20000)
print("This is the rotated array: ", Listy)
print("This is the number being searched: ", search)
print("The number {} is at index: {}".format(search, hopSearch(search, Listy)))