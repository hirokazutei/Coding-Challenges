# 2.1 Remove Dups
# Write Code to remove duplicates from an unsorted linked list.

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

## Simply make a hash table and check (I did not bother implimenting collision solution)
## O(N)

    def removeDupHash(self, node=None):
        if (node == None):
            self.removeDupHash(self.start)
        else:
            if (array[ord(node.data) % length] == 1):
                if (node.pf != None):
                    node.pb.pf = node.pf
                    node.pf.pb = node.pb
                else:
                    node.pb.pf = None
                self.length = self.length - 1
            else:
                array[ord(node.data) % length] = 1
            if (node.pf != None):
                node = node.pf
                self.removeDupHash(node)

# 2.1B How would you solve this problem if a temporary buffer is not allowed?
## Have two searches going on, comparing each variable against the rest of the list.
## O(N**2)

    def removeDupPoint(self):
        nodeA = self.start
        while(nodeA.pf != None):
            nodeB = nodeA.pf
            while(nodeB != None):
                if (nodeA.data == nodeB.data):
                    if (nodeB.pf != None):
                        nodeB.pb.pf = nodeB.pf
                        nodeB.pf.pb = nodeB.pb
                    else:
                        nodeB.pb.pf = None
                    self.length = self.length - 1
                nodeB = nodeB.pf
            if (nodeA.pf == None):
                break
            nodeA = nodeA.pf
        print("Duplicates Removed.")


X = Link()

for i in range(100):
    X.insert(chr(random.randint(97,122)))

print("Length is: " + str(X.length))

#X.removeDupHash()
X.removeDupPoint()

for i in range(X.length):
    print("Posistion " + str(i) + " is " + X.findByPosition(i).data)