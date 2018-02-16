# 8.6 Towers of Hanoi
# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of even larger one).
# You have the following constrains:
#   1. Only one disk can be moved at a time.
#   2. A disk is slid off the top of one tower onto another.
#   3. A disk cannot be placed on top of a smaller one.
# Write a program to move the disksfrom the first tower to the last using stacks.

class Game:

    def __init__(self, disks):
        self.disks = disks
        self.towerA = []
        self.towerB = []
        self.towerC = []
        for size in range(self.disks):
            self.towerA.append(disks - size)

    def __repr__(self):
        return "A: {}\nB: {}\nC: {}\n".format(self.towerA, self.towerB, self.towerC)

    def solve2(self, fromt, tot, tempt):
        tempt.append(fromt.pop())
        print(self)
        tot.append(fromt.pop())
        print(self)
        tot.append(tempt.pop())
        print(self)

    def solve3(self, fromt, tot, tempt):
            self.solve2(fromt, tempt, tot)
            tot.append(fromt.pop())
            print(self)
            self.solve2(tempt, tot, fromt)

    def solve(self, layer = None, fromt = None, tot = None, tempt = None):
        if layer is None:
            layer = self.disks
            fromt = self.towerA
            tot = self.towerB
            tempt = self.towerC
        if layer is 0:
            print("You need more disks to play!")
        elif layer is 1:
            self.towerB.append(self.towerA.pop())
        elif layer is 2:
            self.solve2(fromt, tot, tempt)
        elif layer is 3:
            self.solve3(fromt, tot, tempt)
            return fromt, tempt, tot
        else:
            layer -= 1
            fromt, tempt, tot = self.solve(layer, fromt, tot, tempt) # 1 - 2
            tempt.append(fromt.pop()) # 1 - 3
            print(self)
            if layer % 2 is not 0:
                self.solve(layer, tot, tempt, fromt) # 2 - 3
            else:
                self.solve(layer, tot, fromt, tempt)  # 2 - 3
            return fromt, tot, tempt



    def pop(self, tower):
        if len(tower) is not 0:
            rv = tower[-1]
            tower.pop()


# Displace all until towerA is [], then build up tower B or C
# s2 3, s2, 4, s2 3 - 4, s2

game1 = Game(5)
print(game1)
game1.solve()
print(game1)


