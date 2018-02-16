# 8.5 Recursive Multiply
# Write a recursive function to multiplytwo positive integers without using the * operator.
# You can use addition, subtraction, and bit shifting but you should minimize the number of operations.

class Math:

    @staticmethod
    def multiplyBU(a, b, rv = None): # Bottom Up Approach
        if rv is None:
            rv = 0
        if b is not 1:
            b -= 1
            rv = Math.multiplyBU(a, b, rv)
            return rv + a
        else:
            return a # Base Value of a

    @staticmethod
    def multiplyTD(a, b, value = None): # Top Down Approach
        if value is None:
            value = 0
        if b is not 0:
            value += a
            b -= 1
            result = Math.multiplyTD(a, b, value)
            return result
        else:
            return value # Final Value

print(Math.multiplyTD(20, 8))
