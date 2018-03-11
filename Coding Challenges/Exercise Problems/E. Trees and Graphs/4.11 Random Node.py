# 4.11 Random Node
# You are implementing a binary tree class from scratch, which in addition to insert, find, and delete,
# has a method getRandomNode() which returns a random node from the tree.
# All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode,
# and explain how you would implement the rest of the methods.

import random

class Tree:
    def __init__(self):
        self.nodes = []
        self.length = 0

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data

    def createTree(self, array):
        for item in array:
            node = self.Node(item)
            self.nodes.append(node)
        self.length = len(array)

    def insert(self, node):
        self.nodes.append(node)
        self.length += 1

    def delete(self, position):
        self.nodes[position] = None
       #self.nodes.pop(position)

    def randomNode(self):
        node = self.nodes[random.randint(0, self.length - 1)]
        return node



# Function/Method Call Here:

X = Tree()
arrayA = [3, 1, 2, 0, 5, 4, 6, 7, 1, 2, 0, 0, 8]
X.createTree(arrayA)
print(X.randomNode().data)