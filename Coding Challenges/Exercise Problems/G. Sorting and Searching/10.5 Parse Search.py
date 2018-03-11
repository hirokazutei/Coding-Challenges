# Sparse Search
"""
Given a sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.
"""

# Runtime: O(N log(N))
# Going through the array and clear out the empty strings.

# Runtime: O(N)
# Creating a hash table for non-empty strings.

# Runtime: O(log(N) * avgE) (average empty space)
# finding the next non-empty string


import random

def binaryCrawlSearch(item, array, begin = None, end = None):
    if begin is None:
        begin = 0
        end = len(array) -1
    mid = begin + (end - begin)//2
    if array[begin] is item:
        return begin
    elif array[end] is item:
        return end
    elif array[mid] is item:
        return mid
    else:
        if array[mid] is "":
            mid = searchWord(mid, array)
            if array[mid] is item:
                return mid
        if array[mid] > item:
            return binaryCrawlSearch(item, array, begin + 1, mid - 1)
        elif array[mid] < item:
            return binaryCrawlSearch(item, array, mid + 1, end - 1)

def searchWord(mid, array):
    savemid = mid
    while mid < len(array):
        if array[mid] is not "":
            return mid
        mid += 1
    while savemid >= 0:
        if array[savemid] is not "":
            return savemid
        savemid -= 1
    return False

def insertSpace(array, num):
    length = len(array)
    for word in range(length, 0, -1):
        a = random.randint(0, num)
        for space in range(a):
            array.insert(word, "")
    return words

words = ["at", "ball", "cactus", "disk", "effigy", "flower", "generate", "help",]
search = words[random.randint(0, len(words) - 1)]
words = insertSpace(words, 20)
print("This is the string of array with spaces: ", words)
print("This is the word being searched: ", search)
print("The number {} is at index: {}".format(search, binaryCrawlSearch(search, words)))