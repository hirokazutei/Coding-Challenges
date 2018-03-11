# Stacks & Queue

# Stack: LIFO: last in, first out.
# As far as I know, there are two ways of creating stacks.
# 1. Using a list as stacks.
# 2. Using a linked list as stacks.

## List as Stacks
class ListStack:
    def __init__(self):
        stackList = []

    def push(self, data):
        self.stackList.append(data)

    def pop(self):
        returnV = self.stackList[-1]
        self.stackList.pop()
        return returnV

    def peek(self):
        return self.stackList[-1]

    def isEmpty(self):
        if (self.stackList == []):
            return True
        return False

## Linked List as Stacks
class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    class Node:
        def __init__(self, data, pf = None, pb = None):
            self.data = data
            self.pf = pf
            self.pb = pb

    def push(self, data):
        node = self.Node(data)
        if (self.isEmpty()):
            self.start = node
            self.end = node
        else:
            node.pb = self.end
            self.end.pf = node
            self.end = node

    def peek(self):
        return self.end.data

    def pop(self):
        returnV = self.end
        self.end = self.end.pb
        self.end.pf = None
        return returnV


    def isEmpty(self):
        if (self.start == None):
            return True
        else:
            return False



# Queue: FIFO: first in, first out.
# As far as I know, there are two ways of creating stacks.
# 1. Using a list as stacks.
# 2. Using a linked list as stacks.

## List as Queues
class ListStack:
    def __init__(self):
        stackList = []

    def push(self, data):
        self.stackList.append(data)

    def pop(self):
        if (self.isEmpty()):
            print("List is empty.")
            return False
        else:
            self.stackList.pop(0)

    def peek(self):
        return self.stackList[-1]

    def isEmpty(self):
        if (self.stackList == []):
            return True
        return False

## Linked List as Queues
class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    class Node:
        def __init__(self, data, pf = None, pb = None):
            self.data = data
            self.pf = pf
            self.pb = pb

    def push(self, data):
        node = self.Node(data)
        if (self.isEmpty()):
            self.start = node
            self.end = node
        else:
            node.pb = self.end
            self.end.pf = node
            self.end = node

    def peek(self):
        return self.end.data

    def pop(self):
        returnV = self.start
        self.start.pf.pb = None
        self.start = self.start.pf
        return returnV

    def isEmpty(self):
        if (self.start == None):
            return True
        else:
            return False

