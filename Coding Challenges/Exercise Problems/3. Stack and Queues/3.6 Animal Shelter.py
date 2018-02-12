# 3.6 Animal Shelter
# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.
# People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like.
# Create the data structure to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
# You may use the built-in LinkedList data structure.

import random

class Shelter:
    def __init__(self):
        self.start = None
        self.end = None

    class Node:
        def __init__(self, data):
            self.pf = None
            self.data = data

    def enqueue(self, data):
        node = self.Node(data)
        if (self.start == None):
            self.start = node
            self.end = node
        else:
            self.end.pf = node
            self.end = node

    def dequeueANy(self):
        if (self.end != self.start):
            returnV = self.start
            self.start = self.start.pf
            return self.start
        else:
            self.start = None
            self.end = None
            return self.start

    def dequeueDog(self):
        node = self.start
        if (node.data == "dog"):
            self.start = node.pf
            return node
        while (node.pf != None):
            if (node.pf.data != "dog"):
                node = node.pf
            else:
                temp = node.pf
                if (node.pf != self.end):
                    node.pf = node.pf.pf
                else:
                    node.pf = None
                    self.end = node.pf
                return temp
        print("NO DOGS")

    def dequeueCat(self):
        node = self.start
        if (node.data == "cat"):
            self.start = node.pf
            return node
        while (node.pf != None):
            if (node.pf.data != "cat"):
                node = node.pf
            else:
                temp = node.pf
                if (node.pf != self.end):
                    node.pf = node.pf.pf
                else:
                    node.pf = None
                    self.end = node.pf
                return temp
                print("hfhfh")
        print("NO CATS")

    def printAnimals(self):
        print("\n")
        if (self.start == None):
            print("NO ANIMALS")
        node = self.start
        while(node != None):
            print(node.data)
            node = node.pf

# Function Call etc.:

X = Shelter()

X.enqueue('cat')
X.enqueue('dog')
X.enqueue('cat')
X.enqueue('cat')
X.enqueue('dog')
X.enqueue('cat')
X.enqueue('cat')
X.enqueue('dog')

X.printAnimals()
X.dequeueCat()
X.printAnimals()
X.dequeueCat()
X.printAnimals()
X.dequeueCat()
X.printAnimals()
X.dequeueCat()
X.printAnimals()
X.dequeueCat()
X.printAnimals()
X.dequeueCat()
X.printAnimals()




