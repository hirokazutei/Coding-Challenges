# 26. Reciprocal Cycles

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

# Brainstorm
"""
Think back to when we used to do division by hand. We try to fit the divisor into the remainder, if the divisor is bigger
than the remainder, we add a zero to the end. The subtraction would give us an even division or another remainder.
Theoretically, if the remainder is a number we have encountered before, it will repeat a cycle.
Thus, we can solve this problem by dividing the numbers just like by hand and keeping track of the remainders that
we have encountered.
"""

def ReciprocalCyclesA(num):
    array = [0, 0]
    for i in range(2, num):
        already_divided = []
        count = 0
        remainder = 10
        while True:
            if remainder % i == 0:
                break
            elif remainder // i == 0:
                remainder *= 10
                continue
            else:
                remainder = remainder - i * (remainder // i)
                if remainder in already_divided:
                    break
                already_divided.append(remainder)
                count += 1
        array.append(count)
    largest = max(array)
    for i in range(len(array)):
        if array[i] == largest:
            return i

print(ReciprocalCyclesA(1000))

