# Given an array of distinct integer values, count the number of pairs of integers that have difference K.
# For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).
import random

def generateList(array, size, min, max):
    for i in range(size):
        array.append(random.randint(min, max))

def findPairs(array, k):
    a = max(array)
    lookuptable = [0] * (a + 1)
    for item in array:
        lookuptable[item] = 1
    for item in range(len(lookuptable) - k - 1):
        adjitem = item + 1
        if (lookuptable[adjitem] == 1 and lookuptable[adjitem + k] == 1):
            print("(" + str(adjitem) + ", " + str(adjitem + k) + ")")

array = []
generateList(array, 100, 0, 100)
findPairs(array, random.randint(0, 50))