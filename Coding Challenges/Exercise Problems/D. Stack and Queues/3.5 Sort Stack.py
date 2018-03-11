# 3.5 Sort Stack
# Write a problam to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek and isEmpty.

## We can iterate through the stack but transfering items to the other stack.
## Store min -> max on one stack, store max -> min on the other stack and combine it at the end.
## Proess: O(N**2)

import random

class Stack:
    def __init__(self):
        self.stack = []


    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (self.stack == []):
            print("EMPTY!")
            return
        else:
            returnV = self.stack[-1]
            self.stack.pop()
            return returnV

    def sort(self):
        stackA = []
        num = 0
        min = 0
        max = 0
        while (self.stack != []):
            stackA.append(self.stack.pop())
            num = num + 1
        while (num != 0):
            for times in range(num):
                if (times == 0):
                    max = stackA[-1]
                    stackA.pop()
                else:
                    if (stackA[-1] > max):
                        self.push(max)
                        max = stackA[-1]
                        stackA.pop()
                    else:
                        self.push(stackA[-1])
                        stackA.pop()
            stackA.append(max)
            num = num - 1
            print(self.stack)
            print(stackA)
            if (num == 0):
                break
            for times in range(num):
                if (times == 0):
                    min = self.pop()
                else:
                    temp = self.pop()
                    if (temp < min):
                        stackA.append(min)
                        min = temp
                    else:
                        stackA.append(temp)
            self.push(min)
            num = num - 1
            print(self.stack)
            print(stackA)
        while(stackA != []):
            self.push(stackA[-1])
            stackA.pop()
        return self.stack

# Function/Method Calls Start Here:

X = Stack()

for i in range(20):
    X.push(random.randint(0,30))

print(X.stack)

print(X.sort())