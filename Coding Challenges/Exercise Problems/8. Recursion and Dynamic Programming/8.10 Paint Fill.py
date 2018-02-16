# 8.10 Paint Fill
# Implement the "paint fill" function that one might see on many image editing programs.
# That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
# fill in the surrounding area until the color changes from the original color.

import random

class Screen:
    def __init__(self, col, row, color):
        self.col = col
        self.row = row
        self.pixels = [[color for i in range(col)] for j in range(row)]

    def __repr__(self):
        rv = ' ' + '-' * self.col + '\n'
        for row in range(self.row):
            kv = '|'
            for col in range(self.col):
                kv = kv + str(self.pixels[row][col])
            rv = rv + kv + "|\n"
        rv = rv + ' ' + '-' * self.col + '\n'
        return rv

    def scramble(self, num, probability):
        for i in range(self.row):
            for j in range(self.col):
                a = random.randint(0, 100)
                if a < probability:
                    self.pixels[i][j] = 1

    def paint(self, c, r, color, original = None):
        if original is None:
            original = self.pixels[r][c]
        if c < self.col and r < self.row and c >= 0 and r >= 0:
            if self.pixels[r][c] is original:
                self.pixels[r][c] = color
                self.paint(c + 1, r, color, original)
                self.paint(c - 1, r, color, original)
                self.paint(c, r + 1, color, original)
                self.paint(c, r - 1, color, original)


a = Screen(50, 25, 0)
a.scramble(1, 40)
print(a)

a.paint(10, 5, " ")
print(a)