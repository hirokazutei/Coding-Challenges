# 31. Coin Sums

"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

# Solution A
def CoinSumsA(pounds):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    memo = [[0 for i in range(8)] for j in range(pounds + 1)]
    count = CountRest(pounds, 0, coins, memo)
    return count

def CountRest(remainder, coin, coins, memo):
    count = 0
    if coin < len(coins) - 1:
        for i in range(remainder//coins[coin] + 1):
            new_remainder = remainder -  coins[coin] * i
            if new_remainder == 0:
                count += 1
            elif memo[new_remainder][coin] != 0:
                count += memo[new_remainder][coin]
            else:
                memo[new_remainder][coin] = CountRest(new_remainder, coin + 1, coins, memo)
                count += memo[new_remainder][coin]
        return count
    else:
        return 1


print(CoinSumsA(10000))