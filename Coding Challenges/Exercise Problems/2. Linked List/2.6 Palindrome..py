# 2.6 Palindrome
# Implement a function to check i a linked list is a palindrome.

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


## If the linked list is a doubly linked list, we can compare from the beginning of the list to the middle against the end to the middle.
## Let us assume that we can only use singly linked list.
## We can store the items as a list and compare as a palindrome, which will be the most efficinent process wise.
## Process: O(N)
## Memory: O(N)

    def palindromeList(self):
        list = []
        node = self.start
        while (node != None):
            list.append(node.data)
            node = node.pf
        for data in range(len(list)//2):
            if (list[data] != list[-(data + 1)]):
                return False
        return True


## Alternatively, we can iterate through the list, remember the length of the list and compare each items from both ends.
## Process: O(N**2)
## Memory: O(1)

    def palindromeLinked(self):
        length = self.findLength()
        nodecountA = 0
        nodecountZ = length
        nodeA = self.start
        while(nodecountA < nodecountZ):
            nodeZ = self.start
            for node in range(nodecountZ):
                nodeZ = nodeZ.pf
            if (nodeA.data != nodeZ.data):
                return False
            nodeA = nodeA.pf
            nodecountA = nodecountA + 1
            nodecountZ = nodecountZ - 1
        return True

    def findLength(self, node = None, count = None):
        if (node == None):
            count = 0
            a = self.findLength(self.start, count)
        elif (node.pf == None):
            a = count
            return a
        else:
            count = count + 1;
            newnode = node.pf
            a = self.findLength(newnode, count)
        return a



X = Link()

for i in range(5):
    X.insert(chr(random.randint(97, 98)))

for i in range(X.length):
    print("Posistion " + str(i) + " is " + X.findByPosition(i).data)

print("\nLength is: " + str(X.length) + "\n")

print(X.palindromeList())
print(X.palindromeLinked())
