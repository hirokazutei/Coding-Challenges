# 30 Digit Fifth Numbers
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def DigitFifthNumbers(num):
    squares = [i**num for i in range(10)]
    written = []
    test_num = 10
    while test_num < squares[-1] * len(str(test_num)):
        word = str(test_num)
        total = test_num
        for char in word:
            total -= squares[int(char)]
            if total < 0:
                break
        if total == 0:
            written.append(test_num)
        test_num += 1
    return sum(written)

print(DigitFifthNumbers(5))