# 16.8 English Int
"""
Given any integer, print an English phrase that descries the integer.
"""

import random

number = [' one', ' two', ' three', ' four', ' five', ' six', ' seven', ' eight', ' nine']
hundred = [' hundred']
bigger = ['',  ' thousand', ' million', ' billion', ' trillion']
tens = [' twenty', ' thirty']
ten = [' ten', ' eleven', ' twelve', ' thirteen', 'teen', 'ty']

def english_int(num):
    strnum = str(num)
    digitcount = 0
    word = ''
    threes = ''
    if len(strnum) > 15:
        print("Value too BIG.")
        return False
    for digit in range(len(strnum) - 1, -1, -1):
        if len(threes) < 3:
            threes =  strnum[digit] + threes
        if len(threes) is 3:
            word = below_hundred(threes) + bigger[digitcount] + word
            threes = ''
            digitcount +=1
    if len(threes) is not 0:
        word = below_hundred(threes) + bigger[digitcount] + word
        threes = ''
        digitcount += 1
    return word


def below_hundred(str):
    word = ''
    a = 0
    if len(str) is 3:
        if str[a] is not '0':
            word = word + number[int(str[a]) - 1] + hundred[0]
        a += 1
    if len(str) >= 2:
        if str[a] is not '0':
            if str[a] is '1':
                if int(str[a + 1]) < 4:
                    word = word + ten[int(str[a + 1])]
                    return word
                else:
                    word = word + number[int(str[a + 1])]
                    word = word + ten[4]
            elif int(str[a]) < 4:
                word = word + tens[int(str[a]) - 2]
            else:
                word = word + number[int(str[a]) - 1]
                word = word + ten[5]
        a += 1
    if str[a] is not '0':
        word = word + number[int(str[a]) - 1]
    return word

def generateNum(digits):
    a = 0
    for i in range(digits):
        a += random.randint(0,9) * (10**i)
    return a

randomNum = generateNum(9)
print (randomNum)

print(english_int(randomNum))

