# 8.4 Power Set
# Write a method to retur all subset of a set

class Set:
    def __init__(self, data):
        self.data = data

    def powerSet(self, data = None, array = [], start = 0):
        if data is None:
            print([''])
            self.powerSet(self.data)
        else:
            for item in range(start, len(data)):
                newarray = []
                for things in array:
                    newarray.append(things)
                newarray.append(data[item])
                print(newarray)
                self.powerSet(data, newarray, item + 1)

    def switch(self, a, b):
        tempA = a
        tempB = b
        return tempB, tempA

a = Set(['a', 'b', 'c', 'd'])
a.powerSet()
