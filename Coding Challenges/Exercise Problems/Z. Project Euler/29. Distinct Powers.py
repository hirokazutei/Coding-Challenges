# Distinct Powers

"""
Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""

# Brainstorm
"""

"""

def DistinctPowersA(max):
    powers = set()
    for i in range(2, max + 1):
        for j in range(2, max+1):
            powers.add(i**j)
    return (len(powers))

def DistinctPowersB(max):
    duplicate = 0
    limit = int(max**(1/2) + 1)
    non_squares = [1 for i in range(limit)]
    for i in range(2, int(limit**(1/2)) + 1):
        a = i
        while True:
            a *= i
            if a > limit:
                break
            non_squares[a] = 0
    for i in range(2, len(non_squares)):
        if non_squares[i] == 1:
            times = 1
            n = i
            while n <= 100:
                n *= i
                times += 1
            squares = [0 for i in range(max * (times - 1) + 1)]
            for j in range(1, times):
                a = j
                for k in range(2, max + 1):
                    a += j
                    squares[a] += 1
            for i in squares:
                if i > 1:
                    duplicate += i - 1
            print(squares)
    total = (max - 1)**2 - duplicate
    return total

print(DistinctPowersA(100))
print(DistinctPowersB(100))
