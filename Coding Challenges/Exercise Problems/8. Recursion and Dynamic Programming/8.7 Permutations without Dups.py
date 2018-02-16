# Permutations without Dups
# Write a method to compute all permulations of string of unique characters.

class Permutation:
    def __init__(self, word):
        self.word = word
        self.data = []
        for char in word:
            self.data.append(char)

    def powerSet(self, data = None, array = None):
        if data is None:
            data = []
            array = []
            for things in self.data:
                data.append(things)
        if len(data) is 1:
            array.append(data[0])
            print (array)
            array.pop()
            return
        for things in range(len(data)):
            array.append(data[things])
            temp = data.pop(things)
            self.powerSet(data, array)
            array.pop()
            data.insert(things, temp)

    def switch(self, a, b):
        tempA = a
        tempB = b
        return tempB, tempA

a = Permutation('abca')
a.powerSet()
