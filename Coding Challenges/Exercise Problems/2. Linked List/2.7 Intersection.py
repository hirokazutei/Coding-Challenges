# 2.7 Intersection
# Given two (singly) linked lists, determine if two lists intersect.
# Return the intersecting node.
# Note that intersection is defined based on reference, not value.
# That is, if kth node of the first linked list is the exact same node (by reference) as the jthnode of the second lnked list, then they are intersecting.

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

## If the linked lists are the same length, you can just iterate though the node until you find the same reference.
## O(N)

    def intersectSameLength(self, nodeA, nodeB):
        while(nodeA != None):
            if (nodeA == nodeB):
                return nodeA
            nodeA = nodeA.pf
            nodeB = nodeB.pf
        return False

## But if the linked lists are not the same length, you can find the length and start the search from the same position.

    def intersectFind(self, listA, listB):
        lengthA = 0
        lengthB = 0
        node = listA.start
        while (node != None):
            lengthA = lengthA + 1
            node = node.pf
        node = listB.start
        while (node != None):
            lengthB = lengthB + 1
            node = node.pf
        if (lengthA == lengthB):
            intersect = self.intersectSameLength(listA.start, listB.start)
        elif (lengthA > lengthB):
            dif = lengthA - lengthB
            node = listA.start
            for i in range(dif):
                node = node.pf
            intersect = self.intersectSameLength(node, listB.start)
        elif (lengthA < lengthB):
            dif = lengthB - lengthA
            node = listB.start
            for i in range(dif):
                node = node.pf
            intersect =self.intersectSameLength(listA.start, node)
        return intersect




# Method/Function Calls Here

A = Link()
B = Link()
C = Link()
X = Link()

for i in range(20):
    A.insert(random.randint(0, 9))

for i in range(5):
    B.insert(random.randint(0, 9))

for i in range(5):
    C.insert(random.randint(0, 9))

A.findEnd(A.start).pf = C.start
B.findEnd(B.start).pf = C.start

A.printLink()
B.printLink()

print(X.intersectFind(A, B).data)
