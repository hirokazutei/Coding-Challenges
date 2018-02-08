# 1.6 String Compression
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# You can assume the string has only uppercase and lowercase letters.

stringA = 'aabcccccaaa'
stringB = 'abcaabcaaba'
stringC = 'AAAAAAAAAAAaAA'

## You can just iterate through them linearly and count them.
## Operations: O(N)
## Memory: O(N)

def compressString(string):
    charCount = 1
    wordList = []
    compressed = ''
    for char in range(len(string)):
        if char + 1 == len(string):
            wordList.append(string[char] + str(charCount))
        elif string[char] == string[char + 1]:
            charCount = charCount + 1
        else:
            wordList.append(string[char] + str(charCount))
            charCount = 1
    compressed = (''.join(wordList))
    if len(compressed) < len(string):
        print ("Compressed Word is: " + compressed)
        return compressed
    else:
        print ('Compression did not make the word "' + string + '" shorter.')
        return string

# Function Call
compressString(stringC)
