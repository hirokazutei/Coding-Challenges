# 10.3 Search in Rotated Array
"""
Given a sorted array of n integers that has been rotated by an unknwon number of times,
write code to find an element in the array.
You may assume that the array was originally sorted in increasing order.
"""

import random

# Do a modified binary search

def generateRotatedArray(num):
    array = []
    rotate = random.randint(0,num)
    a = 50
    for numbers in range(num):
        if numbers < rotate:
            a = random.randint(a+1, a + 3)
            array.append(a)
        elif a > 50:
            a = 0
        elif a < 47:
            a = random.randint(a+1, a + 3)
            array.append(a)
        elif a >= 47:
            break
    b = array[random.randint(0, num - 1)]
    return array, b

def modSearch(find, array, begin = None, end = None):
    if begin is None:
        begin = 0
        end = len(array) - 1
    middle = (end - begin)//2 + begin
    if end - begin < 1:
        return False
    if find is array[begin] or find is array[end] or find is array[middle]:
        if array[begin] is find:
            return begin
        elif array[middle] is find:
            return middle
        elif array[end] is find:
            return end
    elif array[middle] < find:
        if array[end] > find:
            rv = modSearch(find, array, middle + 1, end -1)
            if rv is not False:
                return rv
        elif array[end] < find:
            rv =  modSearch(find, array, middle + 1, end -1)
            if rv is not False:
                return rv
            rv = modSearch(find, array, begin + 1, middle -1)
            if rv is not False:
                return rv
    elif array[middle] > find:
        if array[begin] < find:
            rv = modSearch(find, array, begin + 1, middle -1)
            if rv is not False:
                return rv
        elif array[begin] > find:
            rv = modSearch(find, array, middle + 1, end -1)
            if rv is not False:
                return rv
            rv = modSearch(find, array, begin + 1, middle -1)
            if rv is not False:
                return rv

rotatedArray, search = generateRotatedArray(20)
print("This is the rotated array: ", rotatedArray)
print("This is the number being searched: ", search)
print("The number {} is at index: {}".format(search, modSearch(search, rotatedArray)))