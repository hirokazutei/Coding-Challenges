# 10.9 Sorted Matrix Search
"""
Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.
"""

import random

def binaryDiagonalSearch(item, matrix, bcol = None, brow = None, ecol = None, erow = None):
    print(bcol, brow, ecol, erow)
    if bcol is None:
        bcol = 0
        brow = 0
        ecol = len(matrix) - 1
        erow = len(matrix[0]) - 1
    mcol = bcol + (ecol - bcol)//2
    mrow = brow + (erow - brow)//2
    if mcol < 0 or mrow < 0 or mcol >= len(matrix) or mrow >=len(matrix[0]):
        return False, False
    if matrix[bcol][brow] is item:
        return bcol, brow
    elif matrix[mcol][mrow] is item:
        return mcol, mrow
    elif matrix[ecol][erow] is item:
        return ecol, erow
    if (ecol - bcol) < 2:
        col, row = colBinarySearch(item, matrix, ecol, brow, erow)
        if col is not False:
            return col, row
        col, row = colBinarySearch(item, matrix, bcol, brow, erow)
        if col is not False:
            return col, row
    elif erow - brow < 2:
        col, row = rowBinarySearch(item, matrix, erow, bcol, ecol)
        if col is not False:
            return col, row
        col, row = rowBinarySearch(item, matrix, brow, bcol, ecol)
        if col is not False:
            return col, row
    elif item < matrix[mcol][mrow]:
        if item > matrix[mcol-1][mrow-1]:
            col, row = binaryDiagonalSearch(item, matrix, bcol, mrow, mcol - 1, erow)
            if col is not False:
                return col, row
            col, row = binaryDiagonalSearch(item, matrix, mcol, brow, ecol, mrow - 1)
            if col is not False:
                return col, row
        else:
            return binaryDiagonalSearch(item, matrix, bcol, brow, mcol, mrow)
    elif item > matrix[mcol][mrow]:
        if item < matrix[mcol + 1][mrow + 1]:
            col, row = binaryDiagonalSearch(item, matrix, bcol, mrow +1, mcol, erow) ## But it also has to record
            if col is not False:
                return col, row
            col, row = binaryDiagonalSearch(item, matrix, mcol + 1, brow, ecol, mrow) ## It has to start from Zero
            if col is not False:
                return col, row
        else:
            return binaryDiagonalSearch(item, matrix, mcol, mrow, ecol, erow)
    return False, False


def colBinarySearch(item, matrix, col, brow, erow):
    mrow = brow + (erow - brow)//2
    if matrix[col][brow] is item:
        return col, brow
    elif matrix[col][mrow] is item:
        return col, mrow
    elif matrix[col][erow] is item:
        return col, erow
    if erow - brow <= 0:
        return False, False
    if matrix[col][mrow] < item:
        return colBinarySearch(item, matrix, col, mrow + 1, erow - 1)
    if matrix[col][mrow] > item:
        return colBinarySearch(item, matrix, col, brow + 1, mrow - 1)

def rowBinarySearch(item, matrix, row, bcol, ecol):
    mcol = bcol + (ecol - bcol)//2
    if matrix[bcol][row] is item:
        return bcol, row
    elif matrix[mcol][row] is item:
        return mcol, row
    elif matrix[ecol][row] is item:
        return ecol, row
    if ecol - bcol <= 0:
        return False, False
    if matrix[mcol][row] > item:
        return colBinarySearch(item, matrix, row, mcol + 1, ecol - 1)
    if matrix[mcol][row] < item:
        return colBinarySearch(item, matrix, row, bcol + 1, mcol - 1)

def generateMatrix(N, M):
    matrix = [[0 for i in range(N)] for j in range(M)]
    a = 0
    for i in range(len(matrix)):
        if i is not 0:
            a = matrix[i-1][0]
        for j in range(len(matrix[0])):
            if i is 0:
                a = random.randint(a + 1, a + 5)
                matrix[i][j] = a
            elif j is not 0:
                if matrix[i-1][j] >= matrix[i][j-1]:
                    a = matrix[i-1][j]
                else:
                    a = matrix[i][j-1]
            else:
                a = matrix[i-1][j]
            a = random.randint(a + 1, a + 5)
            matrix[i][j] = a
    return matrix

matrix = generateMatrix(6, 6)
matrix = [[8, 15, 18, 22, 32, 38], [10, 17, 23, 28, 36, 39], [15, 21, 28, 29, 41, 45], [19, 22, 30, 32, 43, 49], [24, 29, 35, 36, 45, 53], [25, 33, 39, 44, 50, 56]]
print(matrix)
search = matrix[random.randint(0, len(matrix) -1)][random.randint(0, len(matrix[0]) - 1)]
search = 38
print(search)
print(binaryDiagonalSearch(search, matrix))