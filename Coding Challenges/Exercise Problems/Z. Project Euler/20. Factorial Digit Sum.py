# 20. Factorial Digit Sum

"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

# Brainstorm
"""
This is once again a memory problem. With languages like Pyton, one can simply calculate the factorial of 100 and
add up all the digits.

Otherwise, treat a large number as a list (the simpliest way is to use one index per digit).
"""

# Solution A
def FactorialDigitSumA(digit):
    factorial = 1
    sum = 0
    for i in range(2, digit + 1):
        factorial *= i
    for i in str(factorial):
        sum += int(i)
    return sum

# Solution B
def FactorialDigitSumB(digit):
    factorial = [1]
    sum = 0
    for i in range(2, digit + 1):
        for j in range(len(factorial)):
            factorial[j] *= i
        if factorial[-1] > 9:
            extradigit = len(str(factorial[-1]))
            for digit in range(extradigit-1):
                factorial.append(0)
        for j in range(len(factorial) - 1):
            if factorial[j] > 9:
                factorial[j+1] += factorial[j]//10
                factorial[j] = factorial[j] % 10
    for i in factorial:
        sum += i
    return sum

print(FactorialDigitSumA(100))
print(FactorialDigitSumB(100))