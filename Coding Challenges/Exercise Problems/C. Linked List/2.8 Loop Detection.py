# 2.8 Loop Detection
# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.pf = None
        self.pb = None

class Link:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def insert(self, data, position = None):
        if (position and self.length < position):
            print("Item appended at the end!")
        if (position == None):
            if (self.length == 0):
                newNode = Node(data)
                self.start = newNode
                self.end = newNode
                self.length = 1
            else:
                newNode = Node(data)
                point = self.findEnd(self.start)
                point.pf = newNode
                newNode.pb = point
                self.end = newNode
                self.length = self.length + 1
        else:
            if (position == 0):
                newNode = Node(data)
                newNode.pf = self.start
                self.start.pb = newNode
                self.start = newNode
                self.length = self.length + 1
            elif (self.length > position):
                newNode = Node(data)
                pointb = self.findByPosition(position - 1)
                newNode.pf = pointb.pf
                pointb.pf.pb = newNode
                newNode.pb = pointb
                pointb.pf = newNode
                self.length = self.length + 1
            elif (self.length <= position):
                newNode = Node(data)
                newNode.pb = self.end
                self.end.pf = newNode
                self.end = newNode
                self.length = self.length + 1
            else:
                print("Out of Bound")

    def deleteData(self, data):
        delNode = self.findByData(data)
        print("Item Does Not Exist.")
        if (delNode == -1):
            return -1
        if (delNode.pb == None):
            self.start = delNode.pf
            self.length = self.length - 1
        elif (delNode.pf == None):
            self.end = delNode.pb
            self.length = self.length - 1
        else:
            delNode.pb.pf = delNode.pf
            delNode.pf.pb = delNode.pb
            self.length = self.length - 1

    def deletePosition(self, position):
        delNode = self.findByPosition(position)
        print("Item Does Not Exist.")
        if (delNode == -1):
            return -1
        if (delNode.pb == None):
            self.start = delNode.pf
            self.length = self.length - 1
        elif (delNode.pf == None):
            self.end = delNode.pb
            self.length = self.length - 1
        else:
            delNode.pb.pf = delNode.pf
            delNode.pf.pb = delNode.pb
            self.length = self.length - 1


    def findByData(self, data, start = None):
        if (start == None):
            return self.findByData(data, self.start)
        else:
            if (start.data == data):
                return start
            elif (start.pf == None):
                return -1
            else:
                start = self.findByData(data, start.pf)
                return start

    def findByPosition(self, position):
        if (self.length > position):
            return self.findByPositionB(position, self.start)
        else:
            print ("Out of Bound")
            return -1

    def findByPositionB(self, position, start = None):
        if (position != 0):
            position = position - 1
            start = self.findByPositionB(position, start.pf)
        return start

    def findEnd(self, node):
        if (node.pf != None):
            node = self.findEnd(node.pf)
        return node

    def printLink(self):
        list = []
        node = self.start
        while (node != None):
            list.append(node.data)
            node = node.pf
        print(list)

# Method Start Here
# Let us first determine if there IS indeed a looping linked list by having two runners and see if they intersect.

    def ifLoop(self):
        slowRunner = self.start
        fastRunner = self.start
        found = False
        totalCount = 0
        loopCount = 0
        while (fastRunner != None):
            slowRunner = slowRunner.pf
            fastRunner = fastRunner.pf.pf
            if (found != True):
                totalCount = totalCount + 1
            if (found == True):
                loopCount = loopCount + 1
            if (slowRunner == fastRunner and found == False):
                print(slowRunner.data)
                found = True
            elif (slowRunner == fastRunner and found == True):
                return (totalCount, loopCount)
        return False

## You can determine the loop's length by making the runners run another circle.
## Count the total number, subtract by the length of the circle, start search for the with two runners for the start of the loop.

    def findLoop(self):
        if (self.ifLoop() != False):
            totalCount, loopCount = self.ifLoop()
            print(totalCount)
            print(loopCount)
        else:
            return False
        plus = 0
        startPosition = totalCount - loopCount
        if (startPosition == 0):
            plus = loopCount
        runnerA = self.start
        runnerB = self.start
        for i in range(startPosition):
            runnerA = runnerA.pf
            runnerB = runnerB.pf
        for j in range(loopCount + plus):
            for i in range(loopCount):
                runnerB = runnerB.pf
            if (runnerA == runnerB):
                return runnerA
            runnerA = runnerA.pf
            runnerB = runnerA

X = Link()
length = 10

for i in range(length):
    X.insert(chr(random.randint(97, 123)))

X.printLink()

X.end.pf = X.findByPosition(length - 5)

print(X.findLoop().data)
