# 8.13 Stacks of Boxes
# You have a stack of n boxes, with width wi, height hi, and depth di.
# The boxes cannot be rotated and can only be stacked on top of one another
# if each box in the stack is strictly larger than the boxes above it in width, height, and depth.
# Implement a method to compte the height of the tallest possible stack.
# The height of a stack is the sum of the heights of each box.

import random

class Boxes:

    def __init__(self):
        self.large = []
        self.allboxes = []
        self.beststack = []

    class Box:
        def __init__(self, w, h, d):
            self.w = w
            self.h = h
            self.d = d
            self.small = []

        def __repr__(self):
            return "[{}, {}, {}]".format(self.w, self.h, self.d)

    def makeBoxes(self, number):
        for i in range(number):
            box = self.Box(random.randint(1, 30), random.randint(1, 30), random.randint(1, 30))
            self.allboxes.append(box)
        self.boxTree()

    def boxTree(self):
        for box in range(len(self.allboxes)):
            bigger = False
            for cbox in range(len(self.allboxes)):
                if box is not cbox:
                    if self.allboxes[box].w > self.allboxes[cbox].w and\
                            self.allboxes[box].h > self.allboxes[cbox].h and\
                            self.allboxes[box].d > self.allboxes[cbox].d:
                        self.allboxes[box].small.append(self.allboxes[cbox])
                    if self.allboxes[box].w < self.allboxes[cbox].w and\
                            self.allboxes[box].h < self.allboxes[cbox].h and\
                            self.allboxes[box].d < self.allboxes[cbox].d:
                        bigger = True
            if bigger is False:
                self.large.append(self.allboxes[box])

    def compareBox(self, array = None, combination = None):
        if array is None:
            array = self.large
            combination = []
        for boxes in array:
            combination.append(boxes)
            if len(boxes.small) is 0:
                self.measureup(combination)
                combination.pop()
            else:
                self.compareBox(boxes.small, combination)
                combination.pop()

    def measureup(self, combination):
        total = 0
        for stack in combination:
            total += stack.h
        if len(self.beststack) is 0:
            self.beststack.append(total)
            for item in combination:
                self.beststack.append(item)
        elif self.beststack[0] < total:
            self.beststack = []
            self.beststack.append(total)
            for item in combination:
                self.beststack.append(item)



X = Boxes()
X.makeBoxes(20)
print(X.allboxes)
X.compareBox()
print(X.beststack)