
bigs = "Example: Given a smaller string s and a bigger string b, design an algorithm to find all permutations of the shorter string within the longer one. Print the location of each permutation."
smls = "mht"
slength = len(smls)
blength = len(bigs)
numsmls = 0
table = [0] * 300

for letters in smls:
    numsmls = numsmls + ord(letters)
    table[ord(letters)] = table[ord(letters)] + 1

print (numsmls)

for location in range(0, blength - slength):
    numbigs = 0
    word = ''
    comptable = table
    for letters in range(location, location + slength):
        numbigs = numbigs + ord(bigs[letters])
        word = word + bigs[letters]
    if (numsmls == numbigs):
        found = True
        for char in word:
            comptable[ord(char)] = comptable[ord(char)] - 1
            if (comptable[ord(char)] < 0):
                found = False;
                break;
        if (found):
            print("Match at index: " + str(location + 1))
            print(word)

