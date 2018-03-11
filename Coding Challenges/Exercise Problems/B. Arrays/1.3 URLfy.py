# 1.3 URLfy
# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

string = "Turn this into an URL"
stringwspace = "Turn this into an URL        "
stringlength = len(stringwspace)

# By using a list, we can easily find the appropriate char(s) that we want to replace with something else,
## then join it all together into a string.
## Runtime: O(N)

def listURLfy(string, find, replace):
    flength = len(find)
    urllist = []
    word = 0
    while word < len(string):
        if (word + flength <= len(string) and string[word:word+(flength)] == find):
            urllist.append(replace)
            word = word + flength
        else:
            urllist.append(string[word])
            word = word + 1
    print(''.join(urllist))
    return (''.join(urllist))

## We can also do this the way the problem hinted us to do (and use the inputs given).
## However, I don't quite see how this is necessary.
## O(N)

def stringURLfy(string, find, replace, truelength):
    flength = len(find)
    finalstring = ''
    word = 0
    while 1:
        if (len(finalstring) == truelength):
            break
        if (word + flength <= len(string) and string[word:word+(flength)] == find):
            finalstring = finalstring + replace
            word = word + flength
        else:
            finalstring = finalstring + string[word]
            word = word + 1
    print (finalstring)
    return finalstring


# Function Call
listURLfy(string, ' ', '%20')
stringURLfy(string, ' ', '%20', stringlength)


