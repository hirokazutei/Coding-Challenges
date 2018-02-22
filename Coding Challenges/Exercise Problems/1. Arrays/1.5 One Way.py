# 1.5 One Away
# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# Assuming that lower/upper cases do not matter

# We can simply compare them and do a linear search.
# O(N)

stringA = "Hello, it's me. I was wondering if after all these years you'd like to meet"
stringB = "hello, it's me. i wass wondering if after all these years you'd like to meet"

def oneAway(stringA, stringB, caseSensitive):
    if (caseSensitive != True):
        stringA = stringA.lower()
        stringB = stringB.lower()
    if (len(stringA) == len(stringB)):
        equalCompare(stringA, stringB)
    elif (len(stringA) - 1 == len(stringB)):
        findMissing(stringA, stringB)
    elif (len(stringB) - 1 == len(stringA)):
        findMissing(stringB, stringA)
    else:
        print("More than one char difference away.")

def equalCompare(stringA, stringB):
    if (stringA == stringB):
        print("Same Word.")
        return 1
    else:
        char = 0
        difcount = 0
        difloc = None
        while (char < len(stringA)):
            if (stringA[char] != stringB[char]):
                if (difcount == 1):
                    print("More than one char difference away.")
                    return
                difcount = 1
                difloc = char
            char = char + 1
        print("One character away at index: " + str(difloc))

def findMissing(stringA, stringB):
    char = 0
    difcount = 0
    difloc = None
    skip = 0
    while (char < len(stringB)):
        if (stringA[char+skip] != stringB[char]):
            if (difcount == 1):
                print("More than one char difference away.")
                return
            difcount = 1
            difloc = char
            skip = skip + 1
        char = char + 1
    print("One character away at index: " + str(difloc))


#Function Call
oneAway(stringA, stringB, False)