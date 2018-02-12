# 4.2 Minimal Tree
# Given a sorted (increasing order) array with unique integer elements.
# Write an algorithm to create a binary search tree with minimal height.

import random

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
            pivot = begin + (end - begin)//2
            nodemid = self.Node(array[pivot])
            nodemid.pl = self.binaryIt(array, begin, pivot - 1)
            nodemid.pr = self.binaryIt(array, pivot + 1, end)
            return nodemid

    def printTree(self):
        queue = [self.root, " "]
        while (queue != []):
            if (queue[0] == " "):
                print (" ")
                queue.pop(0)
            else:
                if (queue[0].pl != None):
                    queue.append(queue[0].pl)
                if (queue[0].pr != None):
                    queue.append(queue[0].pr)
                queue.append(" ")
                print(queue[0].data),
                queue.pop(0)

# Function/Method Call Here:

X = Tree()

array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

X.binaryTree(array1)

X.printTree()

