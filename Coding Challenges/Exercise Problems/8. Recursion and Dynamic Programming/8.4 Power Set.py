# 8.4 Power Set
# Write a method to retur all subset of a set

class Set:
    def __init__(self, data):
        self.data = data

    def powerSet(self, remaining = None, data = None):
        if remaining is None:
            remaining = 0
            data = self.data
        if remaining == len(self.data):
            print (data)
        else:
            for item in range(len(data) - remaining):
                data[0], data[item] = self.switch(data[0], data[item])
                self.powerSet(remaining + 1, data)
                data[0], data[item] = self.switch(data[0], data[item])

    def switch(self, a, b):
        tempA = a
        tempB = b
        return tempB, tempA

a = Set(['a', 'b', 'c', 'd'])
a.powerSet()
