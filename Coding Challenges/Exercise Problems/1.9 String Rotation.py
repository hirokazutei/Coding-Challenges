# 1.9 String Rotation
# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
# e.g., "waterbottle" is a rotation of "erbottlewat"


## The limitation that isSubstring can only be used once is actually a big hint.
## The obvious thought is "what should I be checking with isSubstring?"
##      Not the entire word since one is never going to be a substring of another (they are either equal or not a substring).
##      It could be the end of the rotated word but we are not sure where that begins or starts.
##      Makes sense to do a linear search to find the end of the rotated word first.
## O(N)

def findRotation(stringA, stringB):
    charA = 0
    overlapWord = []
    position = 0
    if (stringA == stringB):
        print("These are the same strings.")
        return 1
    elif (len(stringA) != len(stringB)):
        print("These are not rotated strings of each other.")
        return 0
    for charB in range(len(stringB)):
        if (stringA[charA] != stringB[charB]):
            overlapWord = []
            charA = 0
            position = 0
        else:
            overlapWord.append(stringB[charB])
            charA = charA + 1
            if (position == 0):
                position = charB
    if (position == 0):
        print("These are not rotated strings of each other.")
        return 0
    if (isSubstring(stringA, overlapWord)):
        print("These are rotated strings of each other.")
        return 1
    else:
        print("These are not rotated strings of each other.")
        return 0


def isSubstring(string, substring):
    for char in range(len(substring)):
        if (string[char] != substring[char]):
            return False
    return True


findRotation("waterbottle", "ttlewaterbo")