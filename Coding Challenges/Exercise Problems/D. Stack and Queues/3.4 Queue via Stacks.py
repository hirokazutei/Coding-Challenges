# 3.4 Queue Stacks
# Implement a MyQueue class which implements a queue using two stacks

import random

# If you want to access the bottom plate, you simply have to remove the plates on top, place it somewhere else.
# Put the plates back if you want to add a plate to the original top position.

class queueStacks:
    def __init__(self):
        self.stackPush = []
        self.stackPop = []
        self.pushState = True

    def push(self, data):
        if (self.pushState):
            self.stackPush.append(data)
        else:
            self.switchState()
            self.stackPush.append(data)

    def pop(self):
        if (self.pushState):
            self.switchState()
            self.stackPop.pop()
        else:
            self.stackPop.pop()

    def switchState(self):
        if (self.pushState):
            if (self.stackPush == []):
                print("EMPTY!")
                return
            while (self.stackPush != []):
                self.stackPop.append(self.stackPush[-1])
                self.stackPush.pop()
            self.pushState = False
        else:
            if (self.stackPop == []):
                print("EMPTY!")
                return
            while (self.stackPop != []):
                self.stackPush.append(self.stackPop[-1])
                self.stackPop.pop()
            self.pushState = True




X = queueStacks()

for i in range(50):
    X.push(random.randint(0,30))

print(X.stackPop)
print(X.stackPush)

for i in range(5):
    X.pop()

print(X.stackPop)
print(X.stackPush)