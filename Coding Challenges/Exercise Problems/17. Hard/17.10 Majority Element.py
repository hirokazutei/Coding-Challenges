# 17.10 Majority Element

"""
A Majority element is an element that makes up more than half of the items in an array.
Given a positive integers array, find the majority element.
If there is no majority element, return -1.
Do this O(N) time and O(1) space.
"""

import random

def majoritySearch(array):
    candidate = None
    for item in range(len(array)):
        if candidate is None:
            candidate = array[item]
            same = 1
            diff = 0
        else:
            if candidate == array[item]:
                same += 1
            else:
                diff += 1
            if same <= diff:
                candidate = None
    same = 0
    diff = 0
    for item in range(len(array)):
        if array[item] == candidate:
            same += 1
        else:
            diff += 1
    if same > diff:
        return candidate
    else:
        return -1

def generateNum(num):
    array = []
    for i in range(num):
        array.append(random.randint(0,1))
    return array

print(majoritySearch(generateNum(30)))


