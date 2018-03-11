# 1.8 Zero Matrix
# Write an algorithm such that if an element in an M * N matrix is 0, its entire row and columns are set to 0.

import random

matrix = []

def zeroMatrix(matrix):
    clearlistRow = [0] * len(matrix)
    clearlistCol = [0] * len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (matrix[row][col] == 0):
                clearlistRow[row] = 1
                clearlistCol[col] = 1
    for zeroR in range(len(clearlistRow)):
        if clearlistRow[zeroR] == 1:
            for item in range(len(matrix[row])):
                matrix[zeroR][item] = 0
    for zeroC in range(len(clearlistCol)):
        if clearlistCol[zeroC] == 1:
            for item in range(len(matrix)):
                matrix[item][zeroC] = 0
    return matrix

def printMatrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for row in range(height):
        for col in range(width):
            print(matrix[row][col], end=" ")
        print("\n")
    print("\n")


def generateMatrix(matrix, M, N):
    for row in range(M):
        matrix.append([])
        for col in range(N):
            matrix[row].append(random.randint(0, 9))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print(matrix[row][col], end=" ")
        print("\n")
    return matrix

#Function Call
matrix = generateMatrix(matrix, 4, 2)
matrix = zeroMatrix(matrix)
printMatrix(matrix)