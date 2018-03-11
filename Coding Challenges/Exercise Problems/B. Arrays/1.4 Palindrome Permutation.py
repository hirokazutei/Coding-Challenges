# 1.4 Palindrome Permutation
"""
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""

# I have misunderstood the question to print all possible palindrome permutation of a string.


string = "tacooocat"

## Using brute force, we can compute all the possible permutations of a string and check if it is a palindrome.
## O(N! * N)

def brutePalindrome(string):
    string.lower()
    global alist
    global biglist
    palindromelist = []
    alist = list(string)
    biglist = []
    permutate(0)
    for word in biglist:
        word.replace(" ", "")
        palindrome = True
        for char in range(len(word)//2): #The middle character do not matter in a palindrome
            if word[char] != word[-char - 1]:
                palindrome = False
                break
        if (palindrome):
            exist = False
            for existingpalindrome in palindromelist:
                if word == existingpalindrome:
                    exist = True
                    break
            if (exist != True):
                palindromelist.append(word)
    print (palindromelist)

def permutate(num):
    if num == len(alist) - 1:
        biglist.append(''.join(alist))
    else:
        for a in range(num, len(alist), 1):
            alist[a], alist[num] = alist[num], alist[a]
            permutate(num + 1)
            alist[a], alist[num] = alist[num], alist[a]


## We can do so much better!
## The best method I can think of at the moment is to use a hash table to count pairs of characters.
## Use that hashed data to create all permutations of palindromes.
## Best case O(N) if there is no palindrome.
## Worst case O(N!) if there is a palindrome.

hashTable = [0] * 65535

def hashIt(char):
    hashTable[ord(char)] = hashTable[ord(char)] + 1

def checkPalindrome(string):
    global charList
    global palindromeList
    palindromeList = []
    charList = []
    odds = 0
    oddone = ''
    string.lower()
    for char in string:
        hashIt(char)
    for char in string:
        item = hashTable[ord(char)]
        if (item % 2 != 0):
            if (odds == 1):
                print("Palindromes do not exist.")
                return 0
            for times in range(item//2):
                charList.append(char)
            oddone = char
            odds = odds + 1
            hashTable[ord(char)] = 0
        elif (item != 0):
            for times in range(item//2):
                charList.append(char)
            hashTable[ord(char)] = 0
    permutate(0, oddone)
    print(palindromeList)
    return 1

def permutate(num, oddone):
    if (len(charList) - 1 == num):
        newList = []
        for item in charList:
            newList.append(item)
        if (oddone):
            newList.append(oddone)
        for item in range(len(charList)):
            newList.append(charList[-item - 1])
        palindromeList.append(''.join(newList))
        return
    for a in range(num, len(charList), 1):
        charList[a], charList[num] = charList[num], charList[a]
        permutate(num + 1, oddone)
        charList[a], charList[num] = charList[num], charList[a]


# You can use bit manipulation of integers as switches to check if a char is even or odd.


#Function Call
#brutePalindrome(string)
checkPalindrome(string)