# 1.1 Is Unique
"""
Implement an algorithm to determine if a string has all unique characters.
"""

string1 = "AmiUnique?" #Not Unique
string2 = "AEIOU aeiou" #Unique

#  Brute Force
## Of corse, the simple brute force method would be to compare all characters against all other characters.
## Runtime: O(N**2)
## Memory : O(1)

def bruteUnique(string):
    if len(string) > 128: # If the length exceeds the possibilities, it cannot have all unique characters.
        print("Not Unique!")
        return False
    for char in (len(string - 1)):
        for charcomp in (char+1, len(string - 1), 1):
            if char == charcomp: #The program can exit here if it finds a duplicate character.
                print("Not Unique!")
                return False
    print("Unique!")
    return True


#  Hash Table
## A smarter approach would be to simply use a hash table to keep track if a letter has appeared already.
## Runtime: O(N)    Or alternatively: O(C) possible ASCII characters being considered.
## Memory: O(1)

def hashUnique(string):
    if len(string) > 128: # If the length exceeds the possibilities, it cannot have all unique characters.
        print("Not Unique!")
        return False
    hashtable = [0] * 128 # Assuming all possible ASCII characters
    for char in string:
        if hashtable[ord(char)] == 1: # If we have previously encountered this char already...
            print("Not Unique!")
            return False
        hashtable[ord(char)] += + 1 # If we have not encountered this char, add one to hash.
    print("Unique!")
    return True


##### Write a O(N log(N)) function that uses no additional data structures! #####


# Function Call:

hashUnique(string1)
hashUnique(string2)

