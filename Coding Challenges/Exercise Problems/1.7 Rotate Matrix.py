# 1.7 Rotate Matrix
# Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes.
# Write a method to rotate the image by 90 degrees.
# Can you do this in place?

import random

## If N = 10:
##  2, 0 = 10, 2
##  10, 2 = 2, 10
##  8, 10 = 0, 8
##  0, 8 = 8, 0
# From the above pattern, we can see that when rotating o the right, the pattern goes:
# p1(x, y) = p2(N - y, x)

## We can simply divide the image into 4 parts (excluding the center value if the sizes are odd numbered) and switch (rotate) the values.
# O(N**2 * byte)

def rotateR(image):
    height = len(image) - 1
    width = len(image[0]) - 1
    odd = 0
    if (width + 1 % 2 != 0):
        odd = 1
    for byte in range(len(image[height][width])):
        for row in range((height + 1) // 2):
            for col in range((width + 1) // 2 + odd):
                temp = image[row][col][byte]
                image[row][col][byte] = image[height - col][row][byte]
                image[height - col][row][byte] = image[height - row][width - col][byte]
                image[height - row][width - col][byte] = image[col][width - row][byte]
                image[col][width - row][byte] = temp
    return image

def generateImage(N, byte):
    image = []
    for col in range(N):
        image.append([])
        for row in range(N):
            image[col].append([])
            for a in range(byte):
                image[col][row].append([random.randint(0, 9)])
    for a in range(byte):
        print("Layer " + str(a))
        for row in range(N):
            for col in range(N):
                print(image[row][col][a], end=" ")
            print("\n")
        print("\n")
    return image

def printImage(iamge):
    height = len(image)
    width = len(image[0])
    for a in range(len(image[0][0])):
        print("Layer " + str(a))
        for row in range(height):
            for col in range(width):
                print(image[row][col][a], end=" ")
            print("\n")
        print("\n")
    return image


# Function Call
image = generateImage(11, 2)
rotateR(image)
printImage (image)