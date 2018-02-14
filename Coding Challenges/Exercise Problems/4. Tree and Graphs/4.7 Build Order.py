# 4.7 Build Order

import random


def printDependency(fullList):
    print("\nDependency")
    for item in fullList:
        list = []
        for items in range(len(item.dependency)):
            list.append(item.dependency[items].data)
        print(item.data, " ", list)

def printRequiredBy(fullList):
    print("\nRequired By")
    for item in fullList:
        list = []
        for items in range(len(item.requiredBy)):
            list.append(item.requiredBy[items].data)
        print(item.data, " ", list)

def createGraph(fullList):
    for item in range(len(fullList)):
        for items in range(len(fullList)):
            a = random.randint(0, 2000)
            b = random.randint(0, 100)
            if (b >= a and fullList[item] != fullList[items]):
                fullList[item].addDependenBy(fullList[items])

def buildOrder(fullList):
    Root = Node("Root")
    independent = []
    noLoop = Root.checkNodes(independent, fullList)
    if (noLoop != True):
        return False

    order = Root.findOrder()
    if (len(fullList) == len(independent) + len(order)):
        print("\nThe Module can be Built Completely:")
    else:
        print("\nThe Module CANNOT be Built Completely...")
        print("This is the best you can do:")

    print("\nIndependent Nodes")
    list = []
    for item in independent:
        list.append(item.data)
    print(list)

    print("\nBuild Order")
    list = []
    for item in order:
        list.append(item.data)
    print(list)


class Node:
    def __init__(self, data):
        self.data = data
        self.built = False
        self.requiredBy = []
        self.dependency = []

    def setDependency(self, nodes): # Set a node's connection to the given array or single node.
        try:
            if (len(nodes) >= 0):
                self.dependency = nodes
                for item in nodes:
                    item.requiedBy.append(self)
        except TypeError: # Error
            self.dependency = [nodes]
            nodes.requiredBy.append(self)


    def addDependenBy(self, nodes): # insert
        try:
            if (len(nodes) >= 0):
                for item in range(len(nodes) - 1, -1, -1):
                    for existing in self.dependency:
                        if (existing == nodes[item]):
                            nodes.pop(item)
                for item in nodes:
                    self.dependency.append(item)
                    item.requiredBy.append(self)
        except TypeError: # Single Node argument
            for existing in self.dependency:
                if (existing == nodes):
                    return
            self.dependency.append(nodes)
            nodes.requiredBy.append(self)

    # Program that goes through all the nodes and check if they have dependencies
    # Split them into > No Dependency & Not Required > No Dependency & Required > Dependent
    # Loop CANNOT be found this way

    def checkNodes(self, independent, nodelist):
        start = False
        for node in nodelist:
            if (node.dependency == [] and node.requiredBy == []):
                independent.append(node)
            elif (node.dependency == []):
                node.dependency = [self]
                self.requiredBy.append(node)
                start = True
        if (start != True):
            print("Error, there is a loop.")
            return False
        else:
            return True

    def findOrder(self):
        queue = []
        order = []
        for item in self.requiredBy:
            queue.append(item)
            order.append(item)

        print("\nBuild Order")
        list = []
        for item in order:
            list.append(item.data)
        print(list)


        while (queue != []):
            queue[0].built = True
            for depended in range(len(queue[0].requiredBy)):
                if (queue[0].requiredBy[depended].built == False):
                    canBuild = True
                    for dependencies in queue[0].requiredBy[depended].dependency:
                        if (dependencies.built == False):
                            canBuild = False
                    if (canBuild == True):
                        queue[0].requiredBy[depended].built = True
                        queue.append(queue[0].requiredBy[depended])
                        order.append(queue[0].requiredBy[depended])
            queue.pop(0)
        return order


    # All Not Required can be printed separately
    # No Dependency & Required gets connected to rootnode
    # From rootnode, do breadth first crawl until all is met

#Method Call and Functions:

A = Node("A"); B = Node("B"); C = Node("C"); D = Node("D"); E = Node("E"); F = Node("F"); G = Node("G"); H = Node("H"); I = Node("I"); J = Node("J"); K = Node("K"); L = Node("L"); M = Node("M"); N = Node("N"); O = Node("O"); P = Node("P"); Q = Node("Q"); R = Node("R"); S = Node("S"); T = Node("T"); U = Node("U"); V = Node("V"); W = Node("W"); X = Node("X"); Y = Node("Y"); Z = Node("Z");
fullList = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

createGraph(fullList)
#printDependency(fullList)
#printRequiredBy(fullList)
buildOrder(fullList)

