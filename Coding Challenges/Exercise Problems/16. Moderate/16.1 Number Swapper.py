# 16.1 Number Swapper
"""
Write a function to swap a number in place (that is, without using temporary variables).
"""

# We can simply add up the two numbers which allow us to switch variables by subtracting.

def number_swapper(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# There must be a way to do this with bit manipulation as well.


# Function Call Here
a = 5
b = 9
print(a, b)
a, b = number_swapper(a, b)
print(a, b)