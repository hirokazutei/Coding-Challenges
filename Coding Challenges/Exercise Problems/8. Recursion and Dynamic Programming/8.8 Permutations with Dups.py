# Permutations with Dups
# Write a method to compute all permulations of string of unique characters.

class Permutation:
    def __init__(self, word):
        self.word = word
        self.data = []
        for char in word:
            self.data.append(char)

    #Use nodes instead

    def permutate(self, data = None, layer = None):
        if data is None:
            data = []
            layer = 0
            for things in self.data:
                data.append(things)
        if layer is len(data) -1:
            print (data)
            return
        for things in range(layer, len(data)):
            if data[layer] is not data[things] or layer is things:
                data[layer], data[things] = self.switch(data[layer], data[things])
                self.permutate(data, layer + 1)
                data[layer], data[things] = self.switch(data[layer], data[things])


    def switch(self, a, b):
        tempA = a
        tempB = b
        return tempB, tempA

a = Permutation('aacc')
a.permutate()
