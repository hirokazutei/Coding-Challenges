# 32. Pandigital Products

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

# Solution A Super Inefficient
def panDigitalA():
    result = set()
    for a in range(1,99):
       if str(a)[-1] != 1 and str(a)[-1] != 5:
           if '0' not in str(a):
               digits = [n for n in range(1, 10)]
               pandigital = True
               digits2 = [n for n in digits]
               for i in str(a):
                   if int(i) not in digits2:
                       pandigital = False
                       continue
                   else:
                       for j in range(len(digits2) - 1, -1, -1):
                           if int(i) == digits2[j]:
                               digits2.pop(j)
               if pandigital:
                   for b in range(123, 988):
                       if str(b)[-1] != 1 and str(b)[-1] != 5:
                           pandigital = True
                           digits3 = [n for n in digits2]
                           for i in str(b):
                               if int(i) not in digits3:
                                   pandigital = False
                                   continue
                               else:
                                   for j in range(len(digits3) -1, -1, -1):
                                       if int(i) == digits3[j]:
                                           digits3.pop(j)
                           if pandigital:
                               c = a * b
                               if len(str(a)) + len(str(b)) + len(str(c)) != 9:
                                   continue
                               pandigital = True
                               digits4 = [n for n in digits3]
                               for i in str(c):
                                   if int(i) not in digits4:
                                       pandigital = False
                                       continue
                                   else:
                                       for j in range(len(digits4) - 1, -1, -1):
                                           if int(i) == digits4[j]:
                                               digits4.pop(j)
                               if pandigital:
                                   result.add(c)
                                   print(a, b, c)
    return sum(result)

print(panDigitalA())