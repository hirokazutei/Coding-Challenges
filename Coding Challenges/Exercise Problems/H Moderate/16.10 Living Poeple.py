# 16.10 Living People
"""
Given a list f people with their birth and death years, implement a method to compute the year with the most numer of people alive.
You may assume that all people were born between 1900 and 2000 (inclusive.
If a person was alive during any portion of that year, they should be included in that year's count.
For example, person (birth = 1908, death 1909) is included in the counts for both 1908 and 1909.
"""

import random

class Census:

    def __init__(self):
        self.born = [0] * 101
        self.death = [0] * 101
        self.mostPopulation = None
        self.mostYear = None

    def insertYears(self, array):
        for years in array:
            self.born[years[0] - 1900] += 1
            self.death[years[1] - 1900] += 1

    def generatePopulation(self, num):
        array = []
        for times in range(num):
            a = random.randint(1900, 2000)
            array.append([a, random.randint(a, 2000)])
        return array

    def findPopulous(self, array):
        self.insertYears(array)
        count = 0
        max = 0
        maxYear = 0
        for year in range(len(self.born)):
            count += self.born[year]
            if year is not 0:
                count -= self.death[year-1]
            if count > max:
                max = count
                maxYear = year
        self.mostPopulation = max
        self.mostYear = maxYear
        print("During the year {}, there were {} people alive.".format(1900 + maxYear, max))

Canada = Census()
population = Canada.generatePopulation(10000)
Canada.findPopulous(population)