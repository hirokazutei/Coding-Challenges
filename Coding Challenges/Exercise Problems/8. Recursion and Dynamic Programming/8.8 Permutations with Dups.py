# Permutations with Dups
# Write a method to compute all permulations of string of unique characters.

class Permutation:
    def __init__(self, word):
        self.word = word
        self.data = []
        for char in word:
            there = False
            for cchar in range(len(self.data)):
                if self.data[cchar][1] is char:
                    self.data[cchar][0] += 1
                    there = True
            if there is not True:
                self.data.append([1, char])

    def permutate(self, data = None, array = None):
        if data is None:
            data = []
            array = []
            for things in self.data:
                data.append(things)
        total = 0
        for count in range(len(data)):
            total += data[count][0]
            if data[count][0] is 1:
                remaining = count
        if total is 1:
            array.append(data[remaining][1])
            print (array)
            array.pop()
            return
        for things in range(len(data)):
            if data[things][0] is not 0:
                array.append(data[things][1])
                data[things][0] -= 1
                self.permutate(data, array)
                array.pop()
                data[things][0] += 1

    def switch(self, a, b):
        tempA = a
        tempB = b
        return tempB, tempA

a = Permutation('aacc')
print(a.data)
a.permutate()