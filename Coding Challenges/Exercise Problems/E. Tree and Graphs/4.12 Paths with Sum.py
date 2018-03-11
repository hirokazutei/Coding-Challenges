# 4.12 Paths with Sum
# You are given a binary tree in which each node contains an integer value (which might be positive or negative).
# Design an algorithm to count the number of paths that sum to a given value.
# The path does not need to start or end a the root or a leaf, but must go downwards.

# Store value from bottom O(N**2) Memory, O(N**2) Time

class Tree:
    def __init__(self):
        self.root = None

    class Node: #for binary tree
        def __init__(self, data):
            self.data = data
            self.prevAmount = []
            self.pp = None
            self.pl = None # Left Child
            self.pr = None # Right Child

    def createTree(self, array):
        for item in array:
            if self.root == None:
                node = self.Node(item)
                self.root = node
                self.root.prevAmount.append(self.root.data)
            else:
                self.insert(item, self.root)

    def insert(self, item, node):
        queue = [node]
        while (queue != []):
            if queue[0].pl == None:
                newNode = self.Node(item)
                queue[0].pl = newNode
                newNode.pp = queue[0]
                for item in queue[0].prevAmount:
                    newNode.prevAmount.append(item)
                newNode.prevAmount.append(newNode.prevAmount[-1] + newNode.data)
                return
            else:
                queue.append(queue[0].pl)
            if queue[0].pr == None:
                newNode = self.Node(item)
                queue[0].pr = newNode
                newNode.pp = queue[0]
                for item in queue[0].prevAmount:
                    newNode.prevAmount.append(item)
                newNode.prevAmount.append(newNode.prevAmount[-1] + newNode.data)
                return
            else:
                queue.append(queue[0].pr)
            queue.pop(0)
        return


    def sumSearch(self, sum):
        queue = [self.root]
        result = []
        while (queue != []):
            for num in range(len(queue[0].prevAmount) - 1):
                if queue[0].prevAmount[-1] - queue[0].prevAmount[num] == sum:
                    result.append(self.getNode(queue[0], num))
            if queue[0].prevAmount[-1] == sum:
                result.append((queue[0], self.root))
            if queue[0].pl != None:
                queue.append(queue[0].pl)
            if queue[0].pr != None:
                queue.append(queue[0].pr)
            queue.pop(0)
        return result

    def getNode(self, inode, position):
        node = inode
        for i in range(len(inode.prevAmount) - position -1):
            node = node.pp
        return (inode, node)


X = Tree()
arrayA = [5, 1, 2, 0, 5, 4, 6, 7, 1, 2, 0, 0, 8]
X.createTree(arrayA)
print(X.sumSearch(5))