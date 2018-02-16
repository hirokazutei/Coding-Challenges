# 8.9 Parens
# Implement an algorithm to print all valid (e.g., properly opened and closed)combinations of n pairs of parenthesis.

class Parens:
    def __init__(self, num):
        self.num = num

    def parens(self, l = None, r = None, array = None, side = None):
        if array is None:
            array = []
            l = self.num
            r = self.num
        if array is []:
            array.append("(")
            l -= 1
        if side is "(":
            array.append("(")
            l -= 1
        elif side is ")":
            array.append(")")
            r -= 1
        if r is 0 and l is 0:
            print(''.join(array))
            return
        else:
            if l > 0:
                self.parens(l, r, array, "(")
                array.pop()
            if r > 0 and r > l:
                self.parens(l, r, array, ")")
                array.pop()

p = Parens(4)
p.parens()