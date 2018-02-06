#compute all possible values for a^3 + b^3 = c^3 + d^3
import sys
sys.setrecursionlimit(50000)

array = []
size = 100;
divide = size * size * 100

for x in range(divide):
    array.append([0,1,1])

count = 0

def chain(hash, a, b, jump):
    if (hash + jump < len(array)):
        if (array[hash + jump][0] == result):
            print(str(array[hash + 3][1]) + " + " + str(array[hash + 3][2]) + " = " + str(a) + " + " + str(b))
            count = count + 1
        elif (array[hash + jump][0] == 0):
            array[hash + jump] = [result, a, b]
        else:
            chain(hash, a, b, 3)
    else:
        hash = hash - len(array)
        chain(hash, a, b, 3)


for a in range(0, size - 1):
    for b in range (a + 1, size):
        result = (a**3 + b**3)
        hash = result % (divide)
        if (array[hash][0] == result):
            print(str(array[hash][1]) + " + " + str(array[hash][2]) + " = " + str(a) + " + " + str(b))
            count = count + 1
        elif (array[hash][0] == 0):
            array[hash] = [result, a, b]
        else:
            chain(hash, a, b, 3)

print (count)