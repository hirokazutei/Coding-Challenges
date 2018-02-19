# Count of 2s
"""
Write a method to count the number of 2s that appear in all the numbers between 0 and n (inclusive)
"""

def bruteCount(num):
    count = 0
    for numbers in range(num + 1):
        string = str(numbers)
        for char in string:
            if char == '2':
                count += 1
    return count

def smartCount(num):
    count = 0
    string = str(num)
    for digit in range(len(string), 0, -1):
        count += ((digit - 1) * (10 ** (digit - 2)) * int(string[len(string) - digit]))
        if int(string[len(string) - digit]) > 2:
            count += 10 ** (digit - 1)
        elif digit != 1 and int(string[len(string) - digit]) == 2:
            count += int(string[len(string) - (digit - 1):]) + 1
        elif digit == 1 and int(string[len(string) - digit]) == 2:
            count += 1
    return(int(count))

print(smartCount(13222))
print(bruteCount(13222))