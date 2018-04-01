# 25. 1000-digit Fibonacci number

"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

# Brainstorm
"""
I realize that this is a memory problem, but Python can handle extremely large numbers, thus to solve it in python,
it is quite easy. The only difference comes in on the different method one would use to check the digits. The simpliest
form is to turn the number into string and use the len() method. While that is fast in smaller numbers, checking the
floor division or comparing it against 10^digit number would be much faster when the numbers become a certain size.
"""
from _timeit import timeit


# Solution A
@timeit
def FibonacciDigitA(digit):
    a, b = 1, 1
    count = 2
    while len(str(b)) != digit:
        a, b = b, b + a
        count += 1
    return count

# Solution C
@timeit
def FibonacciDigitC(digit):
    a, b = 1, 1
    count = 2
    while True:
        a, b = b, b + a
        count += 1
        try:
            if str(b)[digit-1]:
                return count
        except IndexError:
            continue

# Solution B
@timeit
def FibonacciDigitB(digit):
    a, b = 1, 1
    count = 2
    size = 10 ** (digit - 1)
    while b//(size) < 1:
        a, b = b, b + a
        count += 1
    return count


# Solution D
@timeit
def FibonacciDigitD(digit):
    a, b = 1, 1
    count = 2
    size = 10**(digit-1)
    while b < size:
        a, b = b, b + a
        count += 1
    return count

# Solution E (Memory Sensitive)
@timeit
def FibonacciDigitE(digit):
    fibonacciA = [1]
    fibonacciB = [1]
    count = 2
    while len(fibonacciB) < digit:
        for i in range(len(fibonacciB)):
            fibonacciA[i], fibonacciB[i] = fibonacciB[i], fibonacciA[i] + fibonacciB[i]
        if fibonacciB[-1] > 9:
            fibonacciB.append(0)
            fibonacciA.append(0)
        for j in range(len(fibonacciB) - 1):
            if fibonacciB[j] > 9:
                fibonacciB[j+1] += fibonacciB[j]//10
                fibonacciB[j] = fibonacciB[j] % 10
        count += 1
    return count

print(FibonacciDigitA(1000))
print(FibonacciDigitB(1000))
print(FibonacciDigitC(1000))
print(FibonacciDigitD(1000))
print(FibonacciDigitE(1000))