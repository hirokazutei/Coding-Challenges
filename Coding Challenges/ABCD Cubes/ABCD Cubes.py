#compute all possible values for a^3 + b^3 = c^3 + d^3

array = []
size = 100;
divide = size * size * 10

for x in range(divide):
    array.append([0,1,1])

def chain(array, hash, a, b, jump):
    if (hash + jump < len(array)):
        if (array[hash + jump][0] == result):
            print(str(array[hash + 3][1]) + " + " + str(array[hash + 3][2]) + " = " + str(a) + " + " + str(b))
        elif (array[hash + jump][0] == 0):
            array[hash + jump] = [result, a, b]
        else:
            chain(array, hash, a, b, 3)
    else:
        hash = hash - len(array)
        chain(array, hash, a, b, 3)


for a in range(0, size - 1):
    for b in range (a + 1, size):
        result = (a**3 + b**3)
        hash = result % (divide)
        if (array[hash][0] == result):
            print(str(array[hash][1]) + " + " + str(array[hash][2]) + " = " + str(a) + " + " + str(b))
        elif (array[hash][0] == 0):
            array[hash] = [result, a, b]
        else:
            chain(array, hash, a, b, 3)

