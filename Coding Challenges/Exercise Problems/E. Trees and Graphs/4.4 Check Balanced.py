# 4.4 Check Balanced
# Implement a function to check if a binary tree is balanced.
# For the purpose of this question:
# A balanced tree is defined to be a tree that the heights of the two subtrees of any node never differ by more than one.

import math
import random

class Tree:
    def __init__(self):
        self.root = None

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data
            self.pl = None # Left Child
            self.pr = None # Right Child

# Using what I wrote in the previous function to help me construct a balanced tree.

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

# Writing a method to intentionally create an unbalanced Tree

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

# Using recursion, we can count the nodes from bottom up to the root, with each step comparing the node's left side and right side.
# O(Nodes)

    def checkBalanced(self):
        numbers, unbalanced = self.isBalanced(self.root)
        numbers = numbers + 1
        if (unbalanced != 0):
            if (unbalanced == 1):
                print("There is " + str(unbalanced) + " unbalanced subtrees.")
            else:
                print("There are " + str(unbalanced) + " unbalanced subtrees.")
            return False
        else:
            print("The tree is balanced")
            return True

    def isBalanced(self, node):
        if (node == None):
            return -1, 0
        else:
            unbalanced = 0
            left, a = self.isBalanced(node.pl)
            right, b = self.isBalanced(node.pr)
            left = left + 1
            right = right + 1
            if ((abs(left - right)) > 1):
                unbalanced = 1
            return (left + right), (unbalanced + a + b)


# Function/Method Call Here:

X = Tree()

array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
X.binaryTree(array1)
X.checkBalanced()

Y = Tree()

Y.unbalancedTree(100)
Y.checkBalanced()