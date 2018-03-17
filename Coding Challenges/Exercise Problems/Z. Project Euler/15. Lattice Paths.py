# 15. Lattice paths
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""

# brainstorm

def LatticePathA(num):
    list = [2]
    for i in range(num-1):
        list[0] += 1
        for a in range(1, len(list)):
            list[a] += list[a-1]
        list.append(list[-1]*2)
    return (list[-1])

print(LatticePathA(20))