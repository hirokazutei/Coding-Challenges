# 16.14 Best Line
"""
Given a two-domentional graph with points on it, find a line which passes the most number of points.
"""

import random
import math

def bestLineBrute(points):
    max = 0
    recordPoints = None
    bestSlope = None
    bestIntercept = None
    for start_point in range(len(points)):
        x1 = points[start_point][0]
        y1 = points[start_point][1]
        for compare_point in range(start_point + 1, len(points)):
            count = 0
            x2 = points[compare_point][0]
            y2 = points[compare_point][1]
            if x1 == x2:
                for count_point in range(len(points)):
                    x3 = points[count_point][0]
                    if x3 is x1:
                        count += 1
            else:
                m = (y1 - y2)/(x1 - x2)
                b = y1 - m * x1
                for count_point in range(len(points)):
                    x3 = points[count_point][0]
                    y3 = points[count_point][1]
                    if y3 == round(x3 * m + b):
                        count += 1
            if count > max:
                max = count
                recordPoints = [points[start_point], points[compare_point]]
                bestSlope = m
                bestIntercept = b
    print("The line drawn from {} and {} passes thrugh {} points.".format(recordPoints[0], recordPoints[1], max))


def bestLineBrute(points):
    max = 0
    recordPoints = None
    bestSlope = None
    bestIntercept = None
    for start_point in range(len(points)):
        x1 = points[start_point][0]
        y1 = points[start_point][1]
        for compare_point in range(start_point + 1, len(points)):
            count = 0
            x2 = points[compare_point][0]
            y2 = points[compare_point][1]
            if x1 == x2:
                for count_point in range(len(points)):
                    x3 = points[count_point][0]
                    if x3 is x1:
                        count += 1
            else:
                m = (y1 - y2)/(x1 - x2)
                b = round(y1 - m * x1)
                for count_point in range(len(points)):
                    x3 = points[count_point][0]
                    y3 = points[count_point][1]
                    if y3 == round(x3 * m + b):
                        count += 1
            if count > max:
                max = count
                recordPoints = [points[start_point], points[compare_point]]
                bestSlope = m
                bestIntercept = b
    print("The line drawn from {} and {} passes thrugh {} points.".format(recordPoints[0], recordPoints[1], max))


def bestLine(points):
    max = 0
    bestLine = None
    for start_point in range(len(points)):
        x1 = points[start_point][0]
        y1 = points[start_point][1]
        angles = [1] * 181 #counting self
        lines = [None] * 181
        for compare_point in range(start_point + 1, len(points)):
            x2 = points[compare_point][0]
            y2 = points[compare_point][1]
            if x1 == x2:
                angle = 90
            else:
                angle = round(math.degrees(math.atan((y1-y2)/(x1-x2))))
            angles[int(angle) + 90] += 1
            lines[int(angle) + 90] = (points[start_point], points[compare_point])
        for angle in range(len(angles)):
            if angles[angle] > max:
                max = angles[angle]
                bestLine = lines[angle]
    print("The best line {} passes through {} points.".format(bestLine, max))

def generatePoints(num):
    array = []
    for points in range(num):
        array.append([random.randint(-10000, 10000), random.randint(-10000, 10000)])
    return array

points = generatePoints(3000)
bestLine(points)