#4.10 Check Subtree
# T1 and T2 are two very large binary trees.
# With Y1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical


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





# Function/Method Call Here:

X = Tree()
arrayA = [3, 1, 2, 0, 5, 4, 6, 7, 1, 2, 0, 0, 8]
X.createTree(arrayA)

Y = Tree()
arrayB = [5, 4, 6, 7, 8]
Y.createTree(arrayB)

print(X.startSearch(Y))

