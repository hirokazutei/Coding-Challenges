# 8.12 Eight Queens
# Write an algorithm to print all ways of arranging eight queens on a 8 x 8 chess board so that none of them share the same row, column, or diagonal.
# in this case, "diagonal" means all diagonals, not just two that bisect the board.

class Chess:
    def __init__(self):
        self.col = 8
        self.row = 8
        self.board = [['[ ]' for i in range(8)] for j in range(8)]

    def __repr__(self):
        rv = ''
        for row in range(self.row):
            kv = ''
            for col in range(self.col):
                kv = kv + str(self.board[row][col])
            rv = rv + kv + "\n"
        return rv

    def Queens(self):
        self.insertQ(0, [])

    def insertQ(self, row, queens):
        for col in range(len(self.board[row])):
            if len(queens) is 0:
                queens.append([row, col])
                self.insertQ(row + 1, queens)
                queens = []
            else:
                place = True
                for position in range(len(queens)):
                    if col is queens[position][1]:
                        place = False
                    elif row - col is queens[position][0] - queens[position][1]:
                        place = False
                    elif col + row is queens[position][0] + queens[position][1]:
                        place = False
                if place:
                    queens.append([row, col])
                    if row is 7:
                        print(queens)
                    else:
                        self.insertQ(row + 1, queens)
                    queens.pop()


a = Chess()
print(a)
a.Queens()