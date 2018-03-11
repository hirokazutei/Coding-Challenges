# 3.2 Stack Min
# How would you design a stack which, in addition to push and pop. as a function min, which returns the minimum element?
# Push, pop and min should all operate in O(1) time.

# We can keep track of previously smallest item by having a property on each node.

import random

class ListStack:
    def __init__(self):
        self.stackList = []

    class Node:
        def __init__(self, data, smaller):
            self.data = data
            self.smaller = smaller

    def push(self, data):
        if (len(self.stackList) == 0):
            node = self.Node(data, data)
        else:
            if (self.stackList[-1].smaller <= data):
                node = self.Node(data, self.stackList[-1].smaller)
            else:
                node = self.Node(data, data)
        self.stackList.append(node)

    def pop(self):
        returnV = self.stackList[-1]
        self.stackList.pop()
        return returnV

    def peek(self):
        return self.stackList[-1]

    def min(self):
        return self.stackList[-1].smaller

    def isEmpty(self):
        if (self.stackList == []):
            return True
        return False

X = ListStack()

for i in range(20):
    X.push(random.randint(0,30))
    print(X.stackList[i].data)

print("\n")

for i in range(20):
    print(X.min())
    X.pop()
