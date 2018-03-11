# 4.1 Route Between Nodes
# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.visit = False
        self.point = []

    def setConnections(self, nodes): # Set a node's connection to the given array or single node.
        try:
            if (len(nodes) >= 0):
                self.point = nodes
        except TypeError: # Error
            self.point = [nodes]

    def addConections(self, node): # insert
        try:
            if (len(node) >= 0):
                for item in range(len(node) - 1, -1, -1):
                    for existing in self.point:
                        if (item == existing):
                            node.pop(item)
                for item in node:
                    self.point.append(item)
        except TypeError: # Error
            self.point.append(node)

## To find a path from one node to another, we can apply a Breadth-First-Algorithm
## O(Average number of adjacent nodes ** length)

    def findRoute(self, node2):
        queue = [self]
        while (queue != []):
            for node in queue[0].point:
                if (node == node2):
                    return True
                if (node.visit == False):
                    queue.append(node)
                    node.visit = True
            queue.pop(0)
        return False


## I thought a bidirectional search qould be faster, however, since this graph is directed,
## It could mean that while B has a route to A, A may not have a route to B.

    def findRouteBi(self, node2):
        queueA = [self]
        queueB = [node2]
        while (queueA != [] and queueB != []):
            if (queueA != []):
                for node in queueA[0].point:
                    if (node == node2 or node.visit == 2):
                        print(node.data)
                        return True
                    if (node.visit != 1):
                        queueA.append(node)
                        node.visit = 1
                queueA.pop(0)
            if (queueB != []):
                for node in queueB[0].point:
                    if (node == self or node.visit == 1):
                        print(node.data)
                        return True
                    if (node.visit != 2):
                        queueB.append(node)
                        node.visit = 2
                queueB.pop(0)
        return False


#Method Call and Functions:

A = Node("A"); B = Node("B"); C = Node("C"); D = Node("D"); E = Node("E"); F = Node("F"); G = Node("G"); H = Node("H"); I = Node("I"); J = Node("J"); K = Node("K"); L = Node("L"); M = Node("M"); N = Node("N"); O = Node("O"); P = Node("P"); Q = Node("Q"); R = Node("R"); S = Node("S"); T = Node("T"); U = Node("U"); V = Node("V"); W = Node("W"); X = Node("X"); Y = Node("Y"); Z = Node("Z");
fullList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]


for item in range(len(fullList)):
    for items in range(len(fullList)):
        a = random.randint(0, 550)
        b = random.randint(0, 100)
        if (b >= a and fullList[item] != fullList[items]):
            fullList[item].addConections(fullList[items])

for item in fullList:
    list = []
    for items in range(len(item.point)):
        list.append(item.point[items].data)
    print (item.data, " ", list)

print(A.findRouteBi(B))
