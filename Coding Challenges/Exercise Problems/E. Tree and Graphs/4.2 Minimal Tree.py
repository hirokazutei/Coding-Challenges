# 4.2 Minimal Tree
# Given a sorted (increasing order) array with unique integer elements.
# Write an algorithm to create a binary search tree with minimal height.

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

## The process is very similar to quick-sort.
## Take the middle number and the quater numbers below and above will be the child nodes.
## Organize them otherwise if there are only two nodes.

    def binaryTree(self, array):
        if (len(array) > 2):
            begin = 0
            pivot = len(array)//2
            end = len(array) - 1
            node = self.Node(array[pivot])
            self.root = node
            self.root.pl = self.binaryIt(array, begin, pivot -1)
            self.root.pr = self.binaryIt(array, pivot + 1, end)
        elif (len(array) == 2):
            node = self.Node(array[1])
            self.root = node
            node = self.Node(array[0])
            self.root.pl = node
        else:
            node = self.Node(array[0])
            self.root = node
        return self.root

    def binaryIt(self, array, begin, end):
        if (end - begin == 0):
            nodemid = self.Node(array[end])
            return nodemid
        elif (end - begin == 1):
            nodemid = self.Node(array[end])
            nodeleft = self.Node(array[begin])
            nodemid.pl = nodeleft
            return nodemid
        else:
            pivot = begin + math.ceil((end - begin)/2)
            nodemid = self.Node(array[pivot])
            nodemid.pl = self.binaryIt(array, begin, pivot - 1)
            nodemid.pr = self.binaryIt(array, pivot + 1, end)
            return nodemid

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

# Function/Method Call Here:

X = Tree()

array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

X.binaryTree(array1)

X.printTree()

