# 4.6 Successor

import random
import math

class Tree:
    def __init__(self):
        self.root = None

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data
            self.pp = None # Parent
            self.pl = None # Left Child
            self.pr = None # Right Child

## Using these functions to build binary tress to test
    def binaryTree(self, array):
        if (len(array) > 2):
            begin = 0
            pivot = len(array)//2
            end = len(array) - 1
            node = self.Node(array[pivot])
            self.root = node
            self.root.pl = self.binaryIt(array, begin, pivot -1, node)
            self.root.pr = self.binaryIt(array, pivot + 1, end, node)
        elif (len(array) == 2):
            node = self.Node(array[1])
            self.root = node
            node = self.Node(array[0])
            self.root.pl = node
        else:
            node = self.Node(array[0])
            self.root = node
        return self.root

    def binaryIt(self, array, begin, end, node):
        if (end - begin == 0):
            nodemid = self.Node(array[end])
            nodemid.pp = node
            return nodemid
        elif (end - begin == 1):
            nodemid = self.Node(array[end])
            nodeleft = self.Node(array[begin])
            nodemid.pl = nodeleft
            nodeleft.pp = nodemid
            nodemid.pp = node
            return nodemid
        else:
            pivot = begin + math.ceil((end - begin)/2)
            nodemid = self.Node(array[pivot])
            nodemid.pp = node
            nodemid.pl = self.binaryIt(array, begin, pivot - 1, nodemid)
            nodemid.pr = self.binaryIt(array, pivot + 1, end, nodemid)
            return nodemid

    def printSuccessor(self):
        queue = [self.root]
        while (queue != []):
            list = len(queue)
            for item in range(list):
                if (queue[0].pl != None):
                    queue.append(queue[0].pl)
                if (queue[0].pr != None):
                    queue.append(queue[0].pr)
                if (self.successor(queue[0]) != False):
                    print(queue[0].data, " -> ",  self.successor(queue[0]).data)
                else:
                    print(queue[0].data, " -> Has no next node!")
                queue.pop(0)
            print(" ")

# If right childnode does exist, crawl until the bottom left.
# If right childnode does NOT exist, crawl up one level, if the parent is bigger that is the successor.
# if the parent is smaller, find the parent's parent until you find a successor.

    def successor(self, node):
        compare = node.data
        if (node.pr != None):
            node = node.pr
            while(node.pl != None):
                node = node.pl
            return node
        elif (node.pp != None):
            while(node.pp != None):
                if(compare <= node.pp.data):
                    return node.pp
                node = node.pp
        print("No more next node!")
        return False


X = Tree() #Binary Search Tree
a = random.randint(10, 50)
c = 0
array = []
for i in range(a):
    b = random.randint(c, c+2)
    c = b
    array.append(c)

X.binaryTree(array)
node = X.root.pl.pr.pl
X.printSuccessor()

