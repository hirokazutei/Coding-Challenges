# 1.2 Check Permutation
"""
Given two string, write method to decide if one is a permutation of the other.
"""

stringA = "abcdefghi"
stringB = "ihgfedcba"

# Assumptions
# • It is not case sensitive.

# Brute Force
## Brute Force method involves creating all possible permutations of both strings and comparing them.
## Runtime: O(N!)
## Memory : O(N!)

def permutate(permlist, complist, num = None):
    if num is None:
        num = 0
    if (len(permlist) - 1 == num):
        complist.append(''.join(permlist))
    for a in range(num, len(permlist), 1):
        permlist[a], permlist[num] = permlist[num], permlist[a]
        permutate(permlist, complist, num + 1)
        permlist[a], permlist[num] = permlist[num], permlist[a]

def bruteComparePerm(stringA, stringB):
    if len(stringA) is not len(stringB):
        print("String A is not a permutation of String B!")
        return False
    complist = []
    permlist = list(stringA)
    permutate(permlist, complist)
    for word in complist:
        if word == stringB:
            print("String A is a permutation of String B!")
            return True
    print("String A is not a permutation of String B!")
    return False


## A. Alternatively, a hash table can be used to compare existing characters
## Runtime: O(N)
## Memory : O(1)

hashTable = [0] * 128 #All Possible ASCii Returns for ord(char)

def hashComparePerm(stringA, stringB):
    if len(stringA) is not len(stringB):
        print("String A is not a permutation of String B!")
        return False
    hashIt(stringA)
    for char in stringB:
        if hashTable[ord(char.lower())] is 0:
            print("String A is not a permutation of String B!")
            return False
        else:
            hashTable[ord(char.lower())] -= 1
    print("String A is a permutation of String B!")
    return True

def hashIt(string):
    for char in string:
        hashTable[ord(char)] = hashTable[ord(char)] + 1


##### You can also sort the strings and check the chars: O(N log(N))

## Function Call
bruteComparePerm(stringA, stringB)
hashComparePerm(stringA, stringB)