# 2.5 Sum Lists
# You have two numbers represented by a linked list, where each node contains a single digit.
# The digit are stored in reverse order, such that the 1's digit is at the end of the list.
# write a function that adds the two numbers and returns the sum as a linked list.

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


## Simplest solution is to store the variables in the linked list as an array.
## Transform them into an integer, adding them together and turn it into a linked list.
## Process: O(A + B)
## Memory: O(A + B)

    def sumLink(self, listA, listB, reverse):
        total = self.intoInt(listB.start, reverse) + self.intoInt(listA.start, reverse)
        charIt = str(total)
        if (reverse):
            for char in range(len(charIt)):
                self.insert(charIt[-char - 1])
        else:
            for char in charIt:
                self.insert(char)
        print(total)


    def intoInt(self, node, reverse):
        list = []
        while (node != None):
            list.append(node.data)
            node = node.pf
        integer = 0
        if (reverse):
            for item in range(len(list)):
                integer = integer + list[len(list) - item - 1] * pow(10, item)
        else:
            for item in range(len(list)):
                integer = integer + list[item] * pow(10, item)

        print(integer)
        return integer

## Another solution would be to simply find the length of the list and iterate though them to create the integer.
## Process: O(A**2 + B**2)
## Process Reverse: O(A + B)
## Memory: O(A + B)

    def sumIterate(self, listA, listB, reverse):
        totalInt = self.intoIntIterate(listA, reverse) + self.intoIntIterate(listB, reverse)
        charIt = str(totalInt)
        print(totalInt)
        if (reverse):
            for char in range(len(charIt)):
                self.insert(charIt[-char - 1])
        else:
            for char in charIt:
                self.insert(char)
        print(totalInt)

    def intoIntIterate(self, list, reverse):
        integer = 0
        node = list.start
        if (reverse):
            length = 0
            while (node != None):
                node = node.pf
                length = length + 1
            for items in range(length, 0, -1):
                integer = integer + self.iterateThrough(list.start, items) * pow(10, items)
        else:
            count = 0
            while (node != None):
                integer = integer + node.data * pow(10, count)
                count = count + 1
                node = node.pf
        print(integer)
        return integer

    def iterateThrough(self, node, items):
        for items in range(items, 1, -1):
            node = node.pf
        return node.data

# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem
## I have added a reverse parameter where true/false can be set.


# Method/Function Calls Here

A = Link()
B = Link()
X = Link()

for i in range(5):
    A.insert(random.randint(0, 9))

for i in range(5):
    B.insert(random.randint(0, 9))

for i in range(A.length):
    print("A. Posistion " + str(i) + " is " + str(A.findByPosition(i).data))

for i in range(B.length):
    print("B. Posistion " + str(i) + " is " + str(B.findByPosition(i).data))

#X.sumLink(A, B, False)
X.sumIterate(A, B, False)

for i in range(X.length):
    print("X. Posistion " + str(i) + " is " + str(X.findByPosition(i).data))

