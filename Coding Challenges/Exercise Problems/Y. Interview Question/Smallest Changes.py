# Smallest Change

"""
You are in a hypothetical country where the coin currency comes in strange numbers: 7, 5, 3.
Given a value, what is the least amount of coins you need to meet that value?

For example, 22 can be represented with two 7 coins, one 5 coin, and one 3 coin, totally 4 coins.
"""


def SmallestChange(num, coins):
    array = [0] * (num + 1)
    for i in range(1, num + 1):
        smallest = None
        for c in coins:
            if i - c == 0:
                array[i] = 1
                break
            elif array[i - c] != 0:
                if smallest == None or smallest > array[i-c]:
                    smallest = array[i-c]
            if smallest:
                array[i] = smallest + 1
    return array[-1]

print(SmallestChange(22293, [7, 5, 3]))