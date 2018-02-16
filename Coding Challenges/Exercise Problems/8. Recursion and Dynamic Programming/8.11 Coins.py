# 8.11 Coins
# Given an infinite number of quaters, dimes, nickels and pennies, write code to calculate the number of ways of representing n cents.

class Wallet:
    def __init__(self):
        self.quater = 25
        self.dime = 10
        self.nickel = 5
        self.penny = 1
        self.combination = 0

    def Coins(self, cents):
        self.Quarter(cents,[0, 0, 0, 0])

    def Quarter(self, cents, array):
        max = cents // self.quater
        self.Dime(cents, array)
        for i in range(max):
            cents -= self.quater
            array[0] += 1
            self.Dime(cents, array)

    def Dime(self, cents, array):
        max = cents // self.dime
        self.Nickel(cents, array)
        for i in range(max):
            cents -= self.dime
            array[1] += 1
            self.Nickel(cents, array)
        array[1] = 0

    def Nickel(self, cents, array):
        max = cents // self.nickel
        self.Penny(cents, array)
        for i in range(max):
            cents -= self.nickel
            array[2] += 1
            self.Penny(cents, array)
        array[2] = 0

    def Penny(self, cents, array):
        for i in range(cents):
            array[3] += 1
        print(array)
        array[3] = 0
        self.combination += 1

a = Wallet()
a.Coins(25)
print(a.combination)