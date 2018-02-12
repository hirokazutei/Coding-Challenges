# 3.3 Stack of Plates
# Implement a data structure SetOfStacks that mimics real stacks of plates.
# SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identifally to a single stack (that is, pop() should return the same value as it would if there were just a single stack.)

#FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

import random

class SetOfStacks:
    def __init__(self, size):
        self.set = []
        self.stackCount = []
        self.setNum = 0
        self.size = size

    def push(self, data):
        if (self.set == []):
            self.set.append([])
            self.stackCount.append(0)
            self.set[self.setNum].append(data)
            self.stackCount[self.setNum] = self.stackCount[self.setNum] + 1
        elif (len(self.set[self.setNum]) == self.size):
            self.set.append([])
            self.stackCount.append(0)
            self.setNum = self.setNum + 1
            self.set[self.setNum].append(data)
            self.stackCount[self.setNum] = self.stackCount[self.setNum] + 1
        else:
            self.set[self.setNum].append(data)
            self.stackCount[self.setNum] = self.stackCount[self.setNum] + 1


    def pop(self):
        if (self.setNum == 0 and self.set[self.setNum] == []):
            print("EMPTTY!")
        elif (self.set[self.setNum] == []):
            self.setNum = self.setNum - 1
            self.set.pop()
            returnV = self.set[self.setNum]
            self.set[self.setNum].pop()
            self.stackCount[self.setNum] = self.stackCount[self.setNum] - 1
            return returnV
        else:
            returnV = self.set[self.setNum]
            self.set[self.setNum].pop()
            self.stackCount[self.setNum] = self.stackCount[self.setNum] - 1
            return returnV

    def popAt(self, position):
        stack = 0
        for numbers in self.stackCount:
            if (position < numbers):
                break
            else:
                position = position - numbers
                stack = stack + 1
        if (self.setNum >= stack and len(self.set[stack]) >= position):
            returnV = self.set[stack][position]
            self.set[stack].pop(position)
            self.stackCount[stack] = self.stackCount[stack] - 1
            if (len(self.set[stack]) == 0):
                 self.set.pop(stack)
            return returnV
        print("EMPTTY!")

X = SetOfStacks(20)

for i in range(50):
    X.push(random.randint(0,30))

for i in range(5):
    X.popAt(1)

print(X.set[0])
print(X.set[1])
print(X.set[2])
