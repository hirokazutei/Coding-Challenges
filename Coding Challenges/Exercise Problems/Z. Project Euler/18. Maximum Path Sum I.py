# 18. Maximum Path Sum
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                   75
                  95 64
                 17 47 82
                18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
          99 65 04 28 06 16 70 92
         41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
      53 71 44 65 25 43 91 52 97 51 14
     70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
and requires a clever method!
"""

# Brainstorm
"""
Brute Force Method:
The brute method would be to compute every possible routes and compare the sum of each numbers.
However, as the question has hinted, if the triangle gets any bigger, the computational process will become
too much for any practical use.

Bottom-Up Narrowing Down Method:
We can narrow down our selection from bottom up. For example, the 2nd row from bottom to the left is 63, which
can be connected to 04 or 62. We know for a fact that from 63, working backwards, choosing 04 or 62 would not affect
the range of the chain, thus picking 62 is always better than picking 04 to connect to 63.
"""

data = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Possible Optimal Solution / Solution A
class Triangle:
    def __init__(self, data):
        self.row = None
        self.pyramid = []
        self.nodes = []
        self.GetData(data)
        self.MaximumPath = 0

    def GetData(self, data):
        rows = data.split("\n")
        self.row = -1
        for row in rows:
            self.row += 1
            number = row.split(" ")
            self.pyramid.append(number)
        self.Initialize(self.pyramid)

    class Node:
        def __init__(self, value):
            self.value = int(value)
            self.pdl = None
            self.pdr = None
            self.dul = None
            self.pur = None
            self.chain = []
            self.bigger_value = int(value)

    def Initialize(self, parsed):
        for row in range(len(parsed)):
            temp_array = []
            for item in range(len(parsed[row])):
                node = self.Node(self.pyramid[row][item])
                temp_array.append(node)
            self.nodes.append(temp_array)
        for row in range(len(self.nodes)):
            for item in range(len(self.nodes[row])):
                if row != 0:
                    if item != 0:
                        self.nodes[row][item].pul = self.nodes[row-1][item - 1]
                    if item < len(self.nodes[row]) - 1:
                        self.nodes[row][item].pur = self.nodes[row-1][item]
                if row < len(parsed) - 1:
                    self.nodes[row][item].pdl = self.nodes[row+1][item]
                    self.nodes[row][item].pdr = self.nodes[row+1][item+1]

    def FindMaximumPath(self):
        for i in range(self.row - 1, -1, -1):
            for node in self.nodes[i]:
                if node.pdl.bigger_value > node.pdr.bigger_value:
                    node.bigger_value += node.pdl.bigger_value
                    node.chain.append(node.pdl)
                else:
                    node.bigger_value += node.pdr.bigger_value
                    node.chain.append(node.pdr)
        return A.nodes[0][0].bigger_value

# Optimal Solution Explanation
"""
The time process for this solution is O(N) where if we used brute force, it would be O(N!).
The reason this procedure woult not quite work from top down is because possibilities are expanded as we move down
the triangle, meaning that even if we continuously take the bigger chain from the beginning, bigger values may present
themselves at the end where the chain cannot reach.
On the otherhand, moving from bottom up would eliminate possibilities as we move up, thus when we eliminate a chain
since one from left or right is bigger, we are not eliminating the possiblities that the chain cannot reach a certain location.
"""

A = Triangle(data)
print(A.nodes[A.row-1][0].pdl.bigger_value)
print(A.FindMaximumPath())