



def listing(number):
    number = 4
    array = []
    min = None
    count = 0
    for num in range(number):
        for c in range(num + 1):
            for b in range(num - c + 1):
                a = num - c - b
                if min is None:
                    min = (3**a) * (5**b) * (7**c)
                elif min > (3**a) * (5**b) * (7**c):
                    min = (3**a) * (5**b) * (7**c)
                array.append((3**a) * (5**b) * (7**c))
    print(array)

print(listing(6))
