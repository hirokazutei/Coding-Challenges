# 8. Largest Product in a Series

"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

# Brainstorm
"""
The brute force would be to iterate though the list to multiply every combination of n adjacent numbers.
Though I cannot think of a way to not iterate though every number in the list, there are ways to make the process faster.
1. If the iteration encounters a 0, we can skip to an index one more than where that zero is since anything multiplied
    by 0 is 0. Should the process of skip encounter another zero, repeat the process until a series of non-0 numbers are
    found or it reaches the end of the index.
2. If the number leaving the queue is bigger than the number coming in, the product does not need to be computed
    since the product of those numbers will never be bigger than the previous product.
3. Since arrays take up more computational power to pop the first item, shift items over, etc.
    I have utilized a linked list instead.  
"""

class Series:
    def __init__(self):
        self.numbers = []
        self.largestProduct = []
        self.beginIndex = 0
        self.start = None
        self.end = None
        self.currentProduct = 1
        self.num = 0

    class Link:
        def __init__(self, num, pb = None):
            self.num = num
            self.pf = None
            self.pb = pb

    def SetUp(self, series, num):
        self.num = num
        self.largestProduct = [0] * num
        self.numbers = []
        for i in range(len(series)):
            if series[i].isnumeric():
                self.numbers.append(int(series[i]))
        self.NonZero()
        self.LinkList()
        self.Product()

    def NonZero(self):
        done = False
        while not done:
            done = True
            for l in range(self.num):
                if (l + self.beginIndex) >= len(self.numbers):
                    return False
                elif self.numbers[l + self.beginIndex] == 0:
                    self.beginIndex = l + self.beginIndex + 1
                    done = False
                    break

    def LinkList(self):
        for l in range(self.num):
            if l == 0:
                link = self.Link(self.numbers[l + self.beginIndex])
                self.end = link
            elif l == self.num - 1:
                tlink = link
                link = self.Link(self.numbers[l + self.beginIndex], tlink)
                self.start = link
            else:
                tlink = link
                link = self.Link(self.numbers[l + self.beginIndex], tlink)
        link = self.start
        while link.pb != None:
            link.pb.pf = link
            link = link.pb

    def Product(self):
        link = self.end
        product = 1
        while link != None:
            product *= link.num
            link = link.pf
        if self.currentProduct < product:
            self.currentProduct = product
            link = self.end
            count = 0
            while link != None:
                self.largestProduct[count] = link.num
                count += 1
                link = link.pf

    def Search(self):
        number = self.beginIndex + self.num
        while number < len(self.numbers):
            if self.numbers[number] == 0:
                self.beginIndex = number
                if self.NonZero() == False:
                    break
                number = self.beginIndex - 1
                self.LinkList()
            else:
                old = self.end.num
                new = self.numbers[number]
                self.end = self.end.pf
                self.end.pb = None
                link = self.Link(new, self.start)
                self.start.pf = link
                self.start = link
                if old < new:
                    self.Product()
            number += 1
        return(self.largestProduct, self.currentProduct)

"""
Project Euler did not have an answer to this question.
In addition, on the forums, there were no methods that seemed significantly better optimized than this one.
"""

SeriesA = Series()
SeriesA.SetUp(
"""
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""", 13)

print(SeriesA.Search())