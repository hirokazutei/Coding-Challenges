# 8.2 Robot in a Grid
# Imagine a robot sitting on the upper left corner of grid with r rows and c colums.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them.
# Design an algorithm to find a path for the robot from top left to the bottom right.

import random

class Maze:
    def __init__(self, c, r):
        self.col = c
        self.row = r
        self.structure = [['   ' for i in range(r)] for j in range(c)]
        self.structure[0][0] = ' S '
        self.structure[c-1][r-1] = ' G '

    def __repr__(self):
        rv = ' ' + '---' * maze.row + '\n'
        for row in maze.structure:
            kv = '|'
            for col in row:
                kv = kv + str(col)
            rv = rv + kv + "|\n"
        rv = rv+ ' ' + '---' * maze.row + '\n'
        return rv

    def BlockMaze(self, num):
        for i in range(num):
            c = random.randint(0, self.col - 1)
            r = random.randint(0, self.row - 1)
            if ((c != 0 or r != 0) and (c != self.col - 1 or r!= self.row - 1)):
                self.structure[c][r] = " # "

    def findWay(self, c = 0, r = 0):
        if (c == self.col - 1 and r == self.row - 1):
            self.structure[c][r] = ' O '
            self.structure[0][0] = ' O '
            return True
        elif (c >= self.col or r >= self.row):
            return False
        elif (self.structure[c][r] == " # "):
            return False
        else:
            if (self.findWay(c + 1, r)):
                self.structure[c+1][r] = ' O '
                return True
            elif (self.findWay(c, r+1)):
                self.structure[c][r+1] = ' O '
                return True
        return False


maze = Maze(10, 20)
maze.BlockMaze(30)
print(maze)

print(maze.findWay())

print(maze)