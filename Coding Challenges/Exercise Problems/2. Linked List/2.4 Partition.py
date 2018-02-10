# 2.4 Partition
# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater or equal to x.
# If x is contained within the list, the values of x only need to be after the elements less than x.
# The partition element x can appear anywhere in the right partition, it does not need to appear between the left and right partitions.

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


# METHOD STARTS HERE:

## I guess the question is simply asking us to sort a linked list.
## Without using buffer, you can create two linked list by iterating through them (one bigger or equal to x, one smaller)
## Then simply connect the end of one to the other.
## I won't use doubly linked list features to solve this problem but I will make it compatible.
## O(N)

    def partition(self, x, node = None, smallnode = None, bignode = None, start= None):
        if (node == None and smallnode == None and bignode == None and start == None):
            self.partition(x, self.start)
        elif (node == None):
            if (smallnode == None):
                print("Everything is bigger!")
            elif (start == None):
                print("Everything is smaller!")
            else:
                smallnode.pf = start
        elif (node.data < x):
            if (smallnode == None):
                smallnode = node
                self.start = node
            else:
                tempnode = smallnode
                smallnode = node
                tempnode.pf = smallnode
                smallnode.pb = tempnode
                node.pb = smallnode
            newnode = node.pf
            self.partition(x, newnode, smallnode, bignode, start)
        elif (node.data >= x):
            if (bignode == None):
                bignode = node
                start = node
            else:
                tempnode = bignode
                bignode = node
                tempnode.pf = bignode
                bignode.pb = tempnode
            newnode = node.pf
            self.partition(x, newnode, smallnode, bignode, start)

## There are many solutions to this problem.
    # O(N) Hash Table with another linked list to solve collisions. Then iterate through them to make a new linked list.
    # O(N) Simply iterate through the linked list twice to make one large linked list.
    # O(N**2) Bubble large values back through the list until a large value encounters no values less than the pivot.

# Method/Function Calls Here

X = Link()

for i in range(10):
    X.insert(random.randint(0, 10))

for i in range(X.length):
    print("Posistion " + str(i) + " is " + str(X.findByPosition(i).data))

print("\nLength is: " + str(X.length) + "\n")

X.partition(5)

for i in range(X.length):
    print("Posistion " + str(i) + " is " + str(X.findByPosition(i).data))