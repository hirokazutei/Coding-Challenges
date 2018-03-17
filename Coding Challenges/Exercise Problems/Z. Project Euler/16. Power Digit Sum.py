# Power Digit Sum

"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

# Brainstorm
"""
Some languages like Python,can handle the brute force approach of simply computing the power of 2 to the 1000, then adding the
digits together.

For other languages, we can create a list for each digit and multiply them individually, and let them spill over to the next
digit each exponential multiplication.
"""

# Solution A
def PowerDigitSumA(pow, base):
    array = [0]
    array[0] = 1
    sum = 0
    for i in range(pow):
        for j in range(len(array) - 1, -1, -1):
            array[j] *= base
            if array[j] >= 10:
                if j == len(array) - 1:
                    array.append(array[j]//10)
                else:
                    array[j+1] += array[j]// 10
                array[j] = array[j] % 10
        for k in range(len(array)):
            if array[k] >= 10:
                array[k+1] += array[k]//10
                array[k] = array[k] % 10
    for j in range(len(array)):
        sum += array[j]
    return sum

# Solution B
def PowerDigitSumB(pow, base):
    num = str(base**pow)
    sum = 0
    for i in num:
        sum += int(i)
    return sum

print(PowerDigitSumA(1000, 2))
print(PowerDigitSumB(1000, 2))
