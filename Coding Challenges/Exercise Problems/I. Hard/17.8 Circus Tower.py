# 17.8 Circus Tower
"""
A circus is designing a tower routine consisting of people standing atop one another's shoulders.
For practical and aesthetic reasons, each person must be both shorter and lighter than the person below him or her.
Given the heights and weights of each person in the circus, write a method to compute the largest posible number of people in such tower.
"""

class circus:

    def __init__(self):
        self.acrobats = []
        self.tallest_combination = []
        self.shortest_tallest = []
        self.people = None

    class acrobat:
        def __init__(self, height, weight):
            self.height = height
            self.weidht = weight
            self.stand_on = []
            self.value = 1

    def sortByHeight(self):
        pass

    def findIdealTower(self):
        pass