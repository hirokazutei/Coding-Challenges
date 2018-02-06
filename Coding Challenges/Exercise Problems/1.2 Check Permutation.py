# 1.2 Check Permutation
# Given two string, write method to decide if one is a permutation of the other.

stringA = "abcdefghi"
stringB = "ihgfedcba"

## A. Brute Force method involves creating all possible permutations of both strings and comparing them.
## O(N!) Incredibly inefficient


def permutate(num):
    if (len(permlist) - 1 == num):
        complist.append(''.join(permlist))
    for a in range(num, len(permlist), 1):
        permlist[a], permlist[num] = permlist[num], permlist[a]
        permutate(num + 1)
        permlist[a], permlist[num] = permlist[num], permlist[a]

def crutecCmparePerm(stringA, stringB):
    global permlist
    global complist
    complist = []
    permlist = list(stringA)
    permutate(0)
    for word in complist:
        if word == stringB:
            print("String A is a permutation of String B!")
            return 1
    print("String A is not a permutation of String B!")
    return 0


## A. Alternatively, a hash table can be used to compare existing characters
## O(N) Much Better!

hashTable = [0] * 65535 #All Possible ASCii Returns for ord(char)

def hashComparePerm(stringA, stringB):
    hashIt(stringA)
    for char in stringB:
        if hashTable[ord(char)] == 0:
            print("String A is not a permutation of String B!")
            return 0
        else:
            hashTable[ord(char)] = hashTable[ord(char)] - 1
    print("String A is a permutation of String B!")
    return 1

def hashIt(string):
    for char in string:
        hashTable[ord(char)] = hashTable[ord(char)] + 1


## Function Call
#bruteComparePerm(stringA, stringB)
hashComparePerm(stringA, stringB)