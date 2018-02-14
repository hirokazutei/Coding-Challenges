# 4.8 First Common Ancestor
# Design an algorith and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing additional nodes in data structure.

import random
import math

class Tree:
    def __init__(self):
        self.root = None

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data
            self.pl = None # Left Child
            self.pr = None # Right Child

## Using these functions to build binary tress to test
    def addToTree(self, add):
        node = self.Node(add)
        if (self.root == None):
            self.root = node
            return
        queue = [self.root]
        while (queue != []):
            if (queue[0].pl == None):
                queue[0].pl = node
                return
            elif (queue[0].pr == None):
                queue[0].pr = node
                return
            else:
                queue.append(queue[0].pl)
                queue.append(queue[0].pr)
            queue.pop(0)

    def findAncestor(self, nodeA, nodeB):
        foundA = None
        foundB = None
        ancestor = None
        foundAl = None
        foundBl = None
        ancestorl = None
        foundAr = None
        foundBr = None
        ancestorr = None
        foundAl, foundBl, ancestorl = self.commonAncestor(self.root.pl, nodeA, nodeB)
        foundAr, foundBr, ancestorr = self.commonAncestor(self.root.pr, nodeA, nodeB)
        if (ancestorl != None):
            ancestor = ancestorl
        elif (ancestorr != None):
            ancestor =  ancestorr
        if (self.root == nodeA):
            foundA = nodeA
        elif (foundAl != None):
            foundA = foundAl
        elif (foundAr != None):
            foundA = foundAr
        if (self.root == nodeB):
            foundB = nodeB
        elif (foundBl != None):
            foundB = foundBl
        elif (foundBr != None):
            foundB = foundBr
        if (foundA != None and foundB != None):
            ancestor = self.root
            print("hey")
        if (ancestor != None):
            print(nodeA.data, " and ", nodeB.data, "'s common ancestor is: ", ancestor.data)
            return ancestor
        else:
            print("Somehow could not find Ancestor.")
            return False


    def commonAncestor(self, start, nodeA, nodeB):
        foundA = None; foundB = None; ancestor = None
        foundAl = None; foundBl = None; ancestorl = None
        foundAr = None; foundBr = None; ancestorr = None
        if (start == None):
            return None, None, None
        else:
            foundAl, foundBl, ancestorl = self.commonAncestor(start.pl, nodeA, nodeB)
            foundAr, foundBr, ancestorr = self.commonAncestor(start.pr, nodeA, nodeB)
        if (ancestorl != None):
            return None, None, ancestorl
        if (ancestorr != None):
            return None, None, ancestorr
        if (start == nodeA):
            foundA = nodeA
        elif (foundAl != None):
            foundA = foundAl
        elif (foundAr != None):
            foundA = foundAr
        if (start == nodeB):
            foundB = nodeB
        elif (foundBl != None):
            foundB = foundBl
        elif (foundBr != None):
            foundB = foundBr
        if (foundA != None and foundB!= None):
            return None, None, start
        else:
            if (foundA != None):
                return foundA, None, None
            elif (foundB != None):
                return None, foundB, None
            else:
                return None, None, None

    def printTree(self):
        queue = [self.root]
        while (queue != []):
            list = len(queue)
            for item in range(list):
                if (queue[0].pl != None):
                    queue.append(queue[0].pl)
                if (queue[0].pr != None):
                    queue.append(queue[0].pr)
                print(queue[0].data),
                queue.pop(0)
            print(" ")



X = Tree() #Binary Search Tree
a = random.randint(10, 30)
for i in range(a):
    X.addToTree(random.randint(0, 50))

X.printTree()
X.findAncestor(X.root.pl.pl.pl, X.root.pr.pr.pr)
#print(X.root.pl.pl.data)
