# 16.16 Sub Sort
"""
Given an array of integers, write a method to find indeces m and n such that if you sorted elements m through n, the entire array would be sorted.
Minimize n - m (that is, find the samllest such sequence).
"""

def subSort(array):
    mid = len(array)//2
    maxRange = mid
    minRange = mid
    maxnumStore = mid
    maxnum = mid
    minnumStore = mid
    minnum = mid
    for items in range(mid, len(array)):
        right = array[items]
        if len(array) - items - 1 >= 0:
            left = array[len(array)- items - 1]
            if left < minnumStore:
                minnumStore = left
            elif left > maxnumStore:
                maxnum = left
                maxnumStore = left
                minnum = minnumStore
                minRange = len(array)-items - 1
            if left > minnumStore:
                minnum = minnumStore
                minRange = len(array)-items - 1
        if right > maxnumStore:
            maxNumStore = right
        elif right < minnumStore:
            minnum = right
            minnumStore = right
            maxnum = maxnumStore
            maxRange = items
            if minnum < left:
                minRange = len(array)-items - 1
        if right < maxnumStore:
            maxnum = maxnumStore
            maxRange = items
    print(minRange, maxRange)


subSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])