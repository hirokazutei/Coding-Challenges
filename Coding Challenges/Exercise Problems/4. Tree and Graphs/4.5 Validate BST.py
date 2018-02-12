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

    def unbalancedTree(self, nodes):
        node = self.Node(random.randint(0, 100))
        self.root = node
        queue = [node]
        num = nodes
        while (num > 0 and queue != []):
            list = len(queue)
            for item in range(list):
                if (random.randint(0,100) > 10):
                    node = self.Node(random.randint(0, 100))
                    queue[0].pl = node
                    num = num - 1
                    queue.append(node)
                    if (num < 0):
                        break
                if (random.randint(0,100) > 10):
                    node = self.Node(random.randint(0, 100))
                    queue[0].pr = node
                    num = num - 1
                    queue.append(node)
                    if (num < 0):
                        break
                queue.pop(0)

## Any form of iterating through the nodes of the tree would be acceptable form of validating a binary search tree
## All it has to account for is that the left child node is smaller than its parent node and the right child node is bigger than its parent node.
## Let us utilize a breadth first method.
## Actually, the method is wrong.

    def validateBSTWRONG(self):
        queue = [self.root]
        while (queue != []):
            if (queue[0].pl != None):
                if (queue[0].data <= queue[0].pl.data):
                    print("This tree is NOT a binary search tree.")
                    return False
                queue.append(queue[0].pl)
            if (queue[0].pr != None):
                if (queue[0].data >= queue[0].pr.data):
                    print("This tree is NOT a binary search tree.")
                    return False
                queue.append(queue[0].pr)
            queue.pop(0)
        print("This tree is a binary search tree.")
        return True


## One has to make sure that it isn't JUST the immediate child nodes that are smaller/bigger than the parent node.

    def validateBST(self):
        BST = self.isBST(self.root, None, None)
        if (BST):
            print ("The list is a binary search tree.")
        else:
            print ("The list is NOT a binary search tree.")
        return BST

    def isBST(self, node, min, max):
        if (node == None):
            return True
        if (min != None):
            if (node.pr != None and node.pr.data  < min):
                return False
           # if (node.pl != None and node.pl.data < min):
            #    return False
        if (max != None):
            if (node.pr != None and node.pr.data  > max):
                return False
           # if (node.pl != None and node.pl.data > max):
            #    return False
        left = self.isBST(node.pl, min, node.data)
        right = self.isBST(node.pr, node.data, max)
        if (left and right):
            return True
        else:
            return False


# Function/Method Call Here:

Z = Tree() #Binary Search Tree
array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Z.binaryTree(array1)
Z.validateBST()

X = Tree() #Test case where immediate children nodes are left >= parent >= right
A = X.Node(5); B = X.Node(3); C = X.Node(3); D = X.Node(6); E = X.Node(10); F = X.Node(8); G = X.Node(11); H = X.Node(0);
A.pl = B; B.pl = C; B.pr = D; A.pr = E; E.pl = F; E.pr = G; G.pl = H
X.root = A
X.validateBST()

Y = Tree() #Randomly generated tree
Y.unbalancedTree(100)
Y.validateBST()