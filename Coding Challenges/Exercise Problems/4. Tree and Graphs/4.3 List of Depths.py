# List of Depth:
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.
# e.g., if you have a tree with depth D, you will have D linked lists

import math

class Tree:
    def __init__(self):
        self.root = None

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data
            self.pl = None # Left Child
            self.pr = None # Right Child

# Using what I wrote in the previous function to help me construct a tree.

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

# Use a queue that is split between layers to make linked lists.
# I used breadth first, however, the book seems to want me to do depth first too.
# I will do that later. It is quite easy since with depth first, you can add a layer element to the recursion functions.

    def depthLink(self):
        list = []
        queue = [self.root]
        link = Link(queue[0].data, None)
        list.append(link)
        while (queue != []):
            length = len(queue)
            prev = None
            for item in range(length):
                if (queue[0].pl != None):
                    queue.append(queue[0].pl)
                    if (prev == None):
                        link = Link(queue[0].pl.data, None)
                        list.append(link)
                        prev = link
                    else:
                        link = Link(queue[0].pl.data, None)
                        prev.pf = link
                        prev = link
                if (queue[0].pr != None):
                    queue.append(queue[0].pr)
                    if (prev == None):
                        link = Link(queue[0].pr.data, None)
                        list.append(link)
                        prev = link
                    else:
                        link = Link(queue[0].pr.data, None)
                        prev.pf = link
                        prev = link
                queue.pop(0)
        return list

class Link:
    def __init__(self, data, pf):
        self.data = data
        self.pf = pf

    def iterate(self):
        node = self
        while (node != None):
            print(node.data)
            node = node.pf


# Function/Method Call Here:

X = Tree()

array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

X.binaryTree(array1)
list = X.depthLink()

for item in list:
    print(item.iterate())

