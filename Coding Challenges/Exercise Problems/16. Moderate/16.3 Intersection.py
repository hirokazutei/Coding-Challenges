# 16.3 Intersection
"""
Given two straight line segments (represented as a start point and an end point), compute the pint of intersection, if any.
"""
import random

def mxpb(line):
    horizontal = False
    vertical = False
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    if y1 is y2:
        return False, "hor"
    elif x1 is x2:
        return False, "ver"
    else:
        slope = (y1 - y2)/(x1 - x2)
    b = y1 - x1*slope
    return b, slope

def intersect(lineA, lineB):
    Ax1 = lineA[0][0]
    Ay1 = lineA[0][1]
    Ax2 = lineA[1][0]
    Ay2 = lineA[1][1]
    Bx1 = lineB[0][0]
    By1 = lineB[0][1]
    Bx2 = lineB[1][0]
    By2 = lineB[1][1]
    bA, slopeA = mxpb(lineA)
    bB, slopeB = mxpb(lineB)
    if (slopeA is "hor" and slopeB is "hor") or (slopeA is "ver" and slopeB is "ver"):
        return "Parallel"
    if (bA is False and bB is False):
        if slopeA is "hor":
            x = Bx1
            y = Ay1
        elif slopeB is "hor":
            x = Bx1
            y = Ay1
    elif slopeA is "hor" and bB is not False:
        x = (Ay1 - bB)/slopeB
        y = Ay1
    elif slopeB is "hor" and bB is not False:
        x = (By1 - bA)/slopeA
        y = By1
    elif slopeA is "ver" and bB is not False:
        x = Ax1
        y = Ax1 * slopeB + bB
    elif slopeB is "ver" and bB is not False:
        x = Bx1
        y = Bx1 * slopeA + bA
    elif slopeB is slopeA:
        return "Parallel"
    else:
        x = (bB - bA)/(slopeA - slopeB)
        y = x * slopeA + bA
    if ((x >= Ax1 and x <= Ax2) or (x >= Ax2 and x <= Ax1))\
        and ((x >= Bx1 and x <= Bx2) or (x >= Bx2 and x <= Bx1))\
        and ((y >= Ay1 and y <= Ay2) or (y >= Ay2 and y <= Ay1)) \
        and ((y >= By1 and y <= By2) or (y >= By2 and y <= By1)):
        return x, y
    return False

def makeLines(range):
    return [[random.randint(-range, range), random.randint(-range, range)],\
            [random.randint(-range, range), random.randint(-range, range)]],\
            [[random.randint(-range, range), random.randint(-range, range)], \
             [random.randint(-range, range), random.randint(-range, range)]]

line1, line2 = makeLines(100)
print(line1)
print(line2)
print(intersect(line1, line2))