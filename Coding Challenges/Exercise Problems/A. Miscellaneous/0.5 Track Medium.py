# 0.5 Track Medium
# Numbers are randomly generated and sorted into an (expanding) array.
# How would you keep track of the median

import random
array = []
mintable = []
maxtable = []
tmedian = [None]

def stateMedium(a, b = None):
    if (b == None):
        print("The median is: " + str(a))
    else:
        print("The median is: " + str((a + b)/2))

def trackMedium(newint):
    if (len(mintable) == 0 and len(maxtable) == 0 and tmedian[0] == None):
        tmedian[0] = newint
        stateMedium(newint)
    elif (tmedian[0] != None):
        if (newint >= tmedian[0]):
            maxtable.append(newint)
            bubbleDown(newint, len(maxtable) - 1)
            mintable.append(tmedian[0])
            bubbleUp(newint, len(mintable) - 1)
        elif (newint < tmedian[0]):
            maxtable.append(tmedian[0])
            bubbleDown(newint, len(maxtable) - 1)
            mintable.append(newint)
            bubbleUp(newint, len(mintable) - 1)
        tmedian[0] = None
        stateMedium(mintable[0], maxtable[0])
    elif (tmedian[0] == None and len(mintable) > 0 and len(maxtable) > 0):
        if (newint >= (mintable[0] + maxtable[0])/2):
            if (newint <= maxtable[0]):
                tmedian[0] = newint
                stateMedium(tmedian[0])
            else:
                maxtable.append(newint)
                bubbleDown(newint, len(mintable) - 1)
                tmedian[0] = maxtable[0]
                popmaxbubble()
                stateMedium(tmedian[0])
        elif (newint < (mintable[0] + maxtable[0])/2):
            if (newint >= mintable[0]):
                tmedian[0] = newint
                stateMedium(tmedian[0])
            else:
                mintable.append(newint)
                bubbleUp(newint, len(mintable) - 1)
                tmedian[0] = mintable[0]
                popminbubble()
                stateMedium(tmedian[0])

def bubbleUp(newint, position):
    if (position % 2 != 0):
        minus = 1
    else:
        minus = 2
    parent = int((position - minus)/2)
    if (parent >= 0):
        if (mintable[parent] < newint):
            mintable[parent], mintable[position] = mintable[position], mintable[parent]
            bubbleUp(newint, parent)

def bubbleDown(newint, position):
    if (position % 2 != 0):
        minus = 1
    else:
        minus = 2
    parent = int((position - minus)/2)
    if (parent >= 0):
        if (maxtable[parent] > newint):
            maxtable[parent], maxtable[position] = maxtable[position], maxtable[parent]
            bubbleUp(newint, parent)

def popminbubble():
    mintable[0] = mintable[len(mintable) - 1]
    mintable.pop(-1)
    popbubbleDown(mintable[0], 0)

def popmaxbubble():
    maxtable[0] = maxtable[len(maxtable) - 1]
    maxtable.pop(-1)
    popbubbleUp(maxtable[0], 0)

def popbubbleDown(popped, position):
    childL = position * 2 + 1
    childR = position * 2 + 2
    if (childL < len(mintable) - 1):
        if (childR < len(mintable) - 1):
            if (popped < mintable[childL] or popped < mintable[childR]):
                if (mintable[childL] >= mintable[childR]):
                    mintable[childL], mintable[position] = mintable[position], mintable[childL]
                    popbubbleDown(popped, childL)
                else:
                    mintable[childR], mintable[position] = mintable[position], mintable[childR]
                    popbubbleDown(popped, childR)
        else:
            if (popped < mintable[childL]):
                mintable[childL], mintable[position] = mintable[position], mintable[childL]
                popbubbleDown(popped, childL)

def popbubbleUp(popped, position):
    childL = position * 2 + 1
    childR = position * 2 + 2
    if (childL < len(maxtable) - 1):
        if (childR < len(maxtable) - 1):
            if (popped > maxtable[childL] or popped > maxtable[childR]):
                if (maxtable[childL] <= maxtable[childR]):
                    maxtable[childL], maxtable[position] = maxtable[position], maxtable[childR]
                    popbubbleUp(popped, childL)
                else:
                    maxtable[childR], maxtable[position] = maxtable[position], maxtable[childR]
                    popbubbleUp(popped, childR)
        else:
            if (popped > maxtable[childL]):
                maxtable[childL], maxtable[position] = maxtable[position], maxtable[childL]
                popbubbleUp(popped, childL)

def appendRandom():
    newint = random.randint(0, 100)
    array.append(newint)
    trackMedium(newint)

for i in range(200):
    appendRandom()

print (array)
print (mintable)
print (maxtable)