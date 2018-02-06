# 1.1 Is Unique

# Implement an algorithm to determine if a string has all unique characters.

string1 = "Am I Unique?" #Not Unique
string2 = "AEIOU•aeiou" #Unique

## Of corse, the simple brute force method would be to compare all characters against all other characters.
## O(N**2)
def bruteUnique(string):
    for char in (len(string - 1)):
        for charcomp in (char+1, len(string - 1), 1):
            if char == charcomp: #The program can exit here if it finds a duplicate character.
                print("Not Unique!")
                return 0
    print("Unique!")
    return 1

## A smarter approach would be to simply use a hash table.
## O(N)
def hashUnique(string):
    hashtable = [0] * 65535
    for char in string:
        if hashtable[ord(char)] == 1: #If we have previously encountered this char already...
            print("Not Unique!")
            return 0
        hashtable[ord(char)] = hashtable[ord(char)] + 1
    print("Unique!")
    return 1

hashUnique(string1)
hashUnique(string2)