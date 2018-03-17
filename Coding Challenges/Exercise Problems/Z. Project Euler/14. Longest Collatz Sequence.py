# 14. Longest Collatz sequence

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


# Brainstorm
"""
Brute Force Method:
One can simply iterate through all numbers from 2 to 1 million and calculate how many steps it took from a number to be
reduced to 1 using the Collatz Sequence.

Check-off Method:
We can have a boolean array of 1 million, iterate through all possibilities of the Collatz sequence
and "check" off numbers as we go.
We can use a queue to store the numbers that will have the Collatz sequence applied to in reverse.
Instead of checking if all the number in the array has been found, we can decrement a number until all 1 million
numbers have been found.

Memoization Method:
The more efficient method to to this is to simply make a list of numbers, iterate through 2 to 1 million,
work out the process of Collatz sequence and record the steps it took.
When future numbers encounter a number that has already been worked out, retrieve that number's steps and 
add it to how many steps it took to get to that number.

Memoization Method Possible Optimization:
When we are working out the Collatz sequence, we can record the unknown numbers we encounter and add them to the
memoized list.
"""
from _timeit import timeit

# Solution A
@timeit
def LongestCollatzSequenceA(num):
    check_off = [0] * num #Everything but 0 and 1.
    check_off[2] = 1
    check_off[1] = 1
    count = num - 3
    queue = [2]
    while count != 0 or len(queue) == 0:
        lastnum = queue[0]
        oddpossible = (queue[0] - 1) % 3
        if oddpossible == 0 and (queue[0] - 1)//3 < len(check_off) and check_off[((queue[0] - 1)//3)] == 0 and (queue[0]-1)//3 > 1:
            if (queue[0] - 1)//3 % 2 != 0:
                queue.append((queue[0] - 1)//3)
                check_off[((queue[0] - 1) // 3) - 2] == 1
                count -= 1
        if queue[0] * 2 < len(check_off) and check_off[(queue[0] * 2)] == 0:
            queue.append(queue[0]*2)
            check_off[queue[0]*2] == 1
            count -= 1
        if queue[0] * 2 >= len(check_off):
            queue.append(queue[0]*2)
        queue.pop(0)
    return (lastnum)

# Optimal Solution & Solution B
@timeit
def LongestCollatzSequenceB(num):
    memoize = [0] * (num+1)
    largest = [0, 0]
    for i in range(2, num):
        a = i
        count = 0
        while a != 1:
            if a % 2 == 0:
                a = a//2
            else:
                a = (a*3)+1
            count += 1
            if a < num and memoize[a] != 0:
                count += memoize[a]
                break
        memoize[i] = count
        if largest[1] < count:
            largest[0] = i
            largest[1] = count
    return(largest)

# Solution C
@timeit
def LongestCollatzSequenceC(num):
    memoize = [0] * (num+1)
    largest = [0, 0]
    for i in range(2, num):
        if memoize[i] != 0:
            continue
        a = i
        c = i
        count = 0
        remember = []
        while a != 1:
            if a % 2 == 0:
                a = a//2
            else:
                a = (a*3)+1
            count += 1
            if a < num and memoize[a] != 0:
                count += memoize[a]
                b = 0
                for i in range(len(remember) - 1, 0, -1):
                    b += 1
                    if remember[i] <= num:
                        memoize[remember[i]] = memoize[a] + b
                break
            else:
                remember.append(a)
        memoize[i] = count
        if largest[1] < count:
            largest[0] = c
            largest[1] = count
    return(largest)

# Optimal Solution Explanation
"""
The check-off method uses a queue and appends every possible numbers that can result into a Collatz sequence that end
up wthin 1000000. It did not account for the fact that multiple of any potential number can eventually result within
1000000, thus filling up the queue with numbers that most likely has nothing to do with the answer.
This process is too 
inefficient.

Instead, the memoization method was MUCH faster since it works within the realm of numbers that needs to be checked.
Optimizing it theoretically should have been able to make it faster since it is reducing the amount of processes.
However, appending arrays and iterating through them required more processing power than simply working out the
Collatz sequence and deal with the numbers that come in between later.
"""

#print(LongestCollatzSequenceA(1000000))
print(LongestCollatzSequenceB(1000000))
print(LongestCollatzSequenceC(1000000))
