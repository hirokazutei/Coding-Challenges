# Linked List
# Here is my simple implimentation of a linked list

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





X = Link()

X.insert("b")
X.insert("d")
X.insert("e")
X.insert("f")
X.insert("g")
X.insert("i")
X.insert("c", 1)
X.insert("h", 6)
X.insert("j")
X.insert("a", 0)

print("Start Data is: " + str(X.start.data))
print("End Data is: " + str(X.end.data))
print("Length is: " + str(X.length))

X.deletePosition(8)

print("Start Data is: " + str(X.start.data))
print("End Data is: " + str(X.end.data))
print("Length is: " + str(X.length))

for i in range(X.length):
    print("Posistion " + str(i) + " is " + X.findByPosition(i).data)