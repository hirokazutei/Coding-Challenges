# 21. Amiable Numbers

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

# Brainstorm
"""
Brute Force:
Find the factors of each number from 1 to 1000, add the numbers together and see if the factors of the sum adds up to the
original number.

Sieve:
Repeating the process of finding the factors for all numbers is computationally expensive. We can reduce this by
pre-computing the factors for each number. Then retrieve the sum of their factors and see if it matches with the
factors of their potentially amiable pair.
"""
from _timeit import timeit

# Optimal Solution & Solution A
@timeit
def AmiableNumbersA(num):
    sieve = [[1] for i in range(num+1)]
    amiable_sum = 0
    for i in range(2, int(num//2)):
        a = i
        while a <= num:
            if i != a:
                sieve[a].append(i) #Does not count itself as a factor
            a += i
    for i in range(num + 1):
        total = sum(sieve[i])
        sieve[i].append(total)
    for i in range(len(sieve)):
        if sieve[i][-1] < num - 1 and i == sieve[sieve[i][-1]][-1] and i < sieve[i][-1]:
            if i != sieve[i][-1]: # Prevent so-called perfect numbers
                amiable_sum += i + sieve[i][-1]
    return amiable_sum

# Solution on Project Euler
@timeit
def AmiableNumbersB(num):
    sum = 0
    for a in range(2, num):
        b = SumDivisors(a)
        if b > a:
            if SumDivisors(b) == a:
                sum += a + b
    return int(sum)

def SumDivisors(num):
    sum = 1
    i = 2
    record_num = num
    while i * i <= num and num > 1:
        if num % i == 0:
            j = i * i
            num = num / i
            while num % i == 0:
                j = j*i
                num = num/i
            sum = sum * (j - 1)
            sum = sum / (i - 1)
        if i == 2:
            i = 3
        else:
            i += 2
    if num > 1:
        sum = sum * (num+1)
    return sum - record_num


print(sum([1]))

print(AmiableNumbersA(10000))
print(AmiableNumbersB(10000))




"""
Just checking someone else's code.
Very slow...
"""
import sympy.ntheory
def d(num: int)->int:
    """Get the sum of the divisors of 'num', not including the last divisor which
    is 'num' itself

    :param num: (int): Our input number
    :return: (int): Sum of divisors of 'num'
    """
    return sum(list(sympy.ntheory.divisors(num)[:-1]))

@timeit
def check_amicables(test_nums: int)->set:
    """Run through all the numbers from 1 to 'test_nums' and get the amicable pairs (as 2 item lists)
    into a list.  Converts the final list into a set to weed out the repeated reversed pairs and
    returns the set

    :param test_nums: (int): upper limit to check for amicable pairs
    :return: (set): Set of all the numbers that appeared in the amicable numbers lists
    """
    # 'a' is current number, d(a) is the sum of its divisors
    # if the sum of the sum of the divisors of 'a' equals 'a' BUT
    # a is not equal to the sum of its divisors, then add 'a' and 'd(a)'
    # to the 'list of lists'
    # (hope i worded that right? program works but not sure my comment makes sense.. :-)
    amicables = [[a, d(a)] for a in range(1, test_nums + 1) if (d(d(a)) == a) and (a != d(a))]

    # get an empty set ready for work
    am_set = set()
    # get each of the pairs from the list
    for n1, n2 in amicables:
        am_set.update([n1, n2])  # add them to the set
    # return set to the caller
    return sum(am_set)


testem = 10000
print(check_amicables(testem))
