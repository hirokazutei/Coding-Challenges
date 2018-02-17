# 10.2 Group Anagrams
"""
Write a method to sort an array of strings so that all the anagrams are next to each other
"""

import random

def charCount(string):
    num = 0
    for char in string.lower():
        num += (10 ** (ord(char) - 97)) #Assuming there is no 10 of same characters in a word
    return num

def hashStore(string):
    num = 0
    for char in string.lower():
        num += ord(char)
    HashArray[int(num/300)] += 1

def hash(string):
    num = 0
    for char in string.lower():
        num += ord(char)
    return int(num/300)

#do a pass of array 1 objects == singles
#search within to find duplicates or

def anagramsHash(array):
    noNeedSort = []
    NeedSort = []
    for items in array:
        hashStore(items)
    for items in array:
        if HashArray[hash(items)] == 1:
            noNeedSort.append(items)
        else:
            NeedSort.append(items)
    for string in range(len(NeedSort) - 1):
        for compare in range(string + 1, len(NeedSort)):
            if charCount(NeedSort[string]) == charCount(NeedSort[compare]):
                NeedSort[compare], NeedSort[string + 1] = NeedSort[string + 1], NeedSort[compare]

    array = []
    for items in NeedSort:
        array.append(items)
    for items in noNeedSort:
        array.append(items)
    return array

def generateStrings(num, strings):
    for times in range(num):
        length = random.randint(2, 8)
        word = ''
        for char in range(length):
            word += chr(random.randint(97, 122))
        strings.append(word)

HashArray = [0] * 300
strings = ['wrod', 'drow', 'heyeyeye', 'dwor', 'yo', 'hey', 'oy', 'whatever', 'hye', 'word', 'eyh', 'yoyoy']
#generateStrings(100, strings)

print(strings)
strings = (anagramsHash(strings))
print(strings)