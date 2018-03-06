# 4. Largest Palindrome Product
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Brain Storm
"""
Since the input parameters are two 3-digit numbers, we know that the range of the answer will be from 100 to 999.
The brute force approach is to multiply all combinations from 100 to 999 and find the largest palindrome numbers.
Another method is to iterate through all the palindrome numbers from biggest to smallest and check if they have products
of two three digit numbers.
"""

# Solution A
def NumPalindromeA(min, max):
    biggest = 0
    for i in range(max, min, -1):
        if i**2 < biggest:
            break
        for j in range(i, min, -1):
            if i * j < biggest:
                break
            palindrome = str(i * j)
            if len(palindrome) % 2 is 0:
                additionalIndex = 0
            else:
                additionalIndex = 1
            isPalindrome = True
            for char in range(len(palindrome)//2 - (1 - additionalIndex), -1, -1):
                if palindrome[char] != palindrome[len(palindrome) - char - 1]:
                    isPalindrome = False
                    break
            if isPalindrome and i * j > biggest:
                biggest = i * j
                print(i, j)
    return biggest

# Solution B
def NumPalindromeB(min, max):
    maxRange = max**2
    maxLen = len(str(maxRange))
    palindrome = [None] * maxLen
    for digit in range(maxLen):
        palindrome[digit] = int(str(maxRange)[digit])
    palindrome = MakePalindrome(maxLen, palindrome)
    products = CheckMultiple(palindrome, maxLen, min, max)
    print(products)
    return products[0] * products[1]

def MakePalindrome(maxLen, palindrome):
    if maxLen % 2 is 0:
        additionalIndex = 0
    else:
        additionalIndex = 1
    prevDec = False
    for digit in range(maxLen//2 - (1 - additionalIndex), -1, -1):
        if palindrome[digit] < palindrome[maxLen - digit - 1]:
            palindrome[maxLen - digit - 1] = palindrome[digit]
            prevDec = True
        elif prevDec:
            palindrome[maxLen - digit - 1] = palindrome[digit]
    if prevDec is False:
        first = True
        for digit in range(maxLen // 2 - 1, -1, -1):
            if first:
                palindrome, maxLen = DecrementDigit(digit + additionalIndex, palindrome, maxLen)
                first = False
            palindrome[maxLen - digit - 1] = palindrome[digit]
    return palindrome

def CheckMultiple(palindrome, maxLen, min, max):
    objectiveMin = min
    objectiveMax = max
    total = max**2
    while total > objectiveMin ** 2:
        max = objectiveMax
        min = objectiveMin
        total = 0
        for digit in range(len(palindrome)):
            total += palindrome[digit] * 10**(maxLen - digit - 1)
        if min < total/max:
            min = int(total/max)
        if total**(1/2) < max:
            max = int(total**(1/2))
        if min < 2:
            min = 2
        for i in range(min, max):
            if total % i is 0:
                return i, total//i
        if maxLen % 2 is 0:
            palindrome, maxLen = DecrementDigit((maxLen // 2) - 1, palindrome, maxLen)
        else:
            palindrome, maxLen = DecrementDigit((maxLen // 2), palindrome, maxLen)
    return False

def DecrementDigit(position, palindrome, maxLen):
    while True:
        if position is 0 and palindrome[position] is 0:
            return False
        elif position < 0:
            return palindrome
        else:
            palindrome[position] -= 1
            if position is 0 and palindrome[position] is 0:
                palindrome.pop(0)
                maxLen -= 1
                for item in range(len(palindrome)):
                    palindrome[item] = 9
                return palindrome, maxLen
            elif palindrome[position] < 0:
                palindrome[position] = 9
                palindrome[maxLen - position - 1] = palindrome[position]
                position -= 1
            else:
                palindrome[maxLen - position - 1] = palindrome[position]
                return palindrome, maxLen
    return False


# Optimal Solution
def NumPalindromeC(min, max):
    biggest = 0
    i = max
    while i >= min:
        if i % 11 is 0:
            j = max
            dj = 1
        else:
            j = 990
            dj = 11
        while j >= i:
            if i * j < biggest:
                break
            else:
                palindrome = str(i * j)
                if len(palindrome) % 2 is 0:
                    additionalIndex = 0
                else:
                    additionalIndex = 1
                isPalindrome = True
                for char in range(len(palindrome) // 2 - (1 - additionalIndex), -1, -1):
                    if palindrome[char] != palindrome[len(palindrome) - char - 1]:
                        isPalindrome = False
                        break
                if isPalindrome and i * j > biggest:
                    biggest = i * j
                    print(i, j)
            j -= dj
        i -= 1
    return biggest

# Optimal Solution Explanation
"""
Since palindromes follow the rule that they can be factored by 11...
(Example)
Palindrome = 100000 * x + 10000 * y + 1000 * z + 100 * z + 10 * y + 1 * x
Palindrome = 100001x + 10010y + 1100z
Palindrome = 11(9091x + 910y + 100z)

This means that one of the multiples will have to be a factor of 11.
This can drastically reduce the numbers that need to be tested to find a palindrome.
"""


print(NumPalindromeA(100, 999))
print(NumPalindromeB(100, 999))
print(NumPalindromeC(100, 999))