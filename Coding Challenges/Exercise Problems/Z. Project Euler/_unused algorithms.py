#Unused algorithms

def SumPossible(limit): #Adds all numbers of potential primes
    sum = 5 #representing 2 and 3
    topadd = False
    botadd = False
    candidate_num = limit // 6
    if limit % 6 == 5:
        topadd, botadd = True, True
    elif limit % 6 > 0:
        botadd = True
    sum += ((candidate_num + 1) * 6) * (candidate_num)
    if not botadd:
        sum -= ((candidate_num) * 6) + 1
    if topadd:
        sum += ((candidate_num + 1) * 6) - 1
    return sum
