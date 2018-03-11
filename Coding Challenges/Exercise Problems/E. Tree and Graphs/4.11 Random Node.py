# 4.11 Random Node
# You are implementing a binary tree class from scratch, which in addition to insert, find, and delete,
# has a method getRandomNode() which returns a random node from the tree.
# All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode,
# and explain how you would implement the rest of the methods.

class Tree:
    def __init__(self):
        self.root = None

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data
            self.pl = None # Left Child
            self.pr = None # Right Child

    def createTree(self, array):
        for item in array:
            if self.root == None:
                node = self.Node(item)
                self.root = node
            else:
                self.insert(item, self.root)

    def insert(self, item, node):
        if (node.data > item):
            if node.pl == None:
                newNode = self.Node(item)
                node.pl = newNode
            else:
                self.insert(item, node.pl)
        if (node.data < item):
            if node.pr == None:
                newNode = self.Node(item)
                node.pr = newNode
            else:
                self.insert(item, node.pr)


    def startSearch(self, tree):
        node = self.root
        return self.search(node, tree)

    def search(self, node, tree):
        if (node == None):
            return
        else:
            if (node.data == tree.root.data):
                same = self.compare(node, tree.root)
                if (same == True):
                    return True
            foundl = self.search(node.pl, tree)
            foundr = self.search(node.pr, tree)
        if (foundr or foundl):
            return True
        return False

    def compare(self, nodeA, nodeB):
        if (nodeA == None and nodeB == None):
            return True
        elif (nodeA == None or nodeB == None):
            return False
        elif (nodeA.data == nodeB.data):
            if (self.compare(nodeA.pl, nodeB.pl) and self.compare(nodeA.pr, nodeB.pr)):
                return True
        else:
            return False


## The tree class can store all nodes in a separate array and a random one can be generated from that at O(N)
## The tree calss can keep track of the number of nodes, given a random number between 0 (root) and total nodes,
##  we can identify it's positon.
##      AKA Use an array type of tree


# Function/Method Call Here:

X = Tree()
arrayA = [3, 1, 2, 0, 5, 4, 6, 7, 1, 2, 0, 0, 8]
X.createTree(arrayA)

Y = Tree()
arrayB = [5, 4, 6, 7, 8]
Y.createTree(arrayB)

print(X.startSearch(Y))

