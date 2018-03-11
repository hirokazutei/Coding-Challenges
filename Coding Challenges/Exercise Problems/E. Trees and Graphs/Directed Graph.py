# Directed Graph

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