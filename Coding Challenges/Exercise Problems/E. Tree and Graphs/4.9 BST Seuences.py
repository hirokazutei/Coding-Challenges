# 4.9 BST Sequence
# A binary search tree was created by traversing through an array from left to right and inserting each element.
# Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

import random
import math

class Tree:
    def __init__(self):
        self.root = None

    class BiNode: #for binary tree
        def __init__(self, data):
            self.data = data
            self.pl = None # Left Child
            self.pr = None # Right Child

    class Node:
        def __init__(self, data):
            self.data = data
            self.point = []
            self.available = []

    def createBi(self, array):
        for item in array:
            if self.root == None:
                node = self.BiNode(item)
                self.root = node
            else:
                self.insertBi(item, self.root)

    def insertBi(self, item, node):
        if (node.data > item):
            if node.pl == None:
                newNode = self.BiNode(item)
                node.pl = newNode
            else:
                self.insertBi(item, node.pl)
        if (node.data < item):
            if node.pr == None:
                newNode = self.BiNode(item)
                node.pr = newNode
            else:
                self.insertBi(item, node.pr)


    def sequenceTree(self, newTree):
        rootnode = self.Node(self.root.data)
        newTree.root = rootnode
        self.createTree(self.root, rootnode)

    def createTree(self, node, new):
        if (node == None):
            return
        elif (node.pl != None or node.pr != None):
            if (node.pl != None):
                new.available.append(node.pl)
            if (node.pr != None):
                new.available.append(node.pr)
        if (len(new.available) == 0):
            return
        things = 0
        for things in range(len(new.available)):
            newnode = self.Node(new.available[things].data)
            for item in new.available:
                newnode.available.append(item)
            new.point.append(newnode)
            newnode.available.pop(things)
            self.createTree(new.available[things], newnode)

    def printPossible(self, node = None, array = None):
        if (node == None):
            node = self.root
            array = [node.data]
            self.printPossible(node, array)
        elif (len(node.point) == 0):
            print (array)
        else:
            for item in node.point:
                newarray = []
                for items in array:
                    newarray.append(items)
                newarray.append(item.data)
                self.printPossible(item, newarray)

# Function/Method Call Here:

Z = Tree() #Binary Search Tree
array = [3, 1, 2, 0, 5, 4, 6]
Z.createBi(array)

X = Tree()
Z.sequenceTree(X)
X.printPossible()