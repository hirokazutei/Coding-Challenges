# 2.2 Return Kth
# Implement an algorithm to find the kth to last element of a signly linked list.


import random

length = 1000
array = [0]*length


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


# METHOD STARTS HERE:

## If we keep track of the length of the list, we can simply find the length-kth node.
## If we did not keep track of the length of the list, we can iterate through the list and return a length.
## O(N)

    def listLength(self, node = None, length = None):
        if (node == None and length == None):
            length = 0
            length = self.listLength(self.start, 0)
        else:
            if(node.pf != None):
                start = length
                node = node.pf
                length = self.listLength(node, length) + 1
            elif(node.pf == None):
                return 1
        return length

## Otherwise, it is also possible to have two pointers at k distance.
## When we iterate through the list and when the second one reaches the end, the first pointer will be the kth element.
## O(N)

    def findKth(self, position):
        pointA = self.start
        pointB = self.start
        for k in range(position - 1):
            pointB = pointB.pf
        while (pointB.pf != None):
            pointA = pointA.pf
            pointB = pointB.pf
        return pointA.data


# Method/Function Calls Here

X = Link()

for i in range(20):
    X.insert(chr(i + 97))

print("Length is: " + str(X.length))

print(X.listLength())
print(X.findKth(10))

for i in range(X.length):
    print("Posistion " + str(i) + " is " + X.findByPosition(i).data)