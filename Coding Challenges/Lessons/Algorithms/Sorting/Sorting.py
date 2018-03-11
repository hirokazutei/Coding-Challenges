import random

def insertionSort(array):
    for item in range(len(array)):
        for compare in range(item, 0, -1):
            if (array[compare - 1] > array[compare]):
                switch(compare, compare - 1)


def selectionSort(array):
    for item in range(len(array)):
        minimum = array[item]
        index = item
        for min in range(item, len(array)):
            if (minimum > array[min]):
                index = min
                minimum = array[min]
        switch(item, index)


def bubbleSort(array):
    iteration = 0
    count = -1
    while (count != 0):
        count = 0
        for item in range((len(array) - 1) - iteration):
           if (array[item] > array[item + 1]):
               switch(item, item + 1)
               count = count + 1
        iteration = iteration + 1



def quickSort(array, minimum = None, maximum = None):
    if minimum is None:
        quickSort(array, 0, len(array) - 1)
    else:
        if (maximum - minimum == 1): #This is if there are only two left
            if (array[minimum] > array[maximum]):
                switch(minimum, maximum)
        elif (maximum - minimum == 2):
            pivot = findPivot(minimum, maximum);
            switch(((minimum + maximum)//2), pivot)
            if (array[maximum] < array[minimum]):
                switch(minimum, maximum)
        else:
            pivot = findPivot(minimum, maximum);
            switch(maximum, pivot)
            position = -1
            stop = -1
            count = 1
            for larger in range(minimum, maximum - 1):
                if (stop >= 0 and stop <= larger):
                    break
                if (array[larger] >= array[maximum]):
                    for smaller in range(maximum - count, minimum, -1):
                        count = count + 1
                        if (smaller <= larger):
                            stop = larger
                            break
                        if (array[smaller] <= array[maximum]):
                            switch(larger, smaller)
                            position = smaller
                            break
            if (stop >= 0):
                switch(stop, maximum)
                if (stop - minimum > 1):
                    quickSort(array, minimum, stop - 1)
                if (maximum - stop > 1):
                    quickSort(array, stop + 1, maximum)
            elif (array[position] > array[maximum]):
                switch(pivot, maximum)
                if (maximum - stop > 1):
                    quickSort(array, stop + 1, maximum)

def findPivot(minimum, maximum):
    a = array[minimum]
    b = array[(maximum + minimum) // 2]
    c = array[maximum]
    if (b >= a >= c or c >= a >= b):
        return minimum
    elif (a >= b >= c or c >= b >= a):
        return (minimum + maximum) // 2
    else:
        return maximum

def switch(a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def generateList(array, size, min, max):
    for i in range(size):
        array.append(random.randint(min, max))

def check(array):
    for i in range(len(array) - 2):
        if (array[i] > array[i+1]):
            print("SORING ALGORITHM FAILED\n")
            print(array[i])
            return -1
    print("SORTING ALGORITHM SUCCESS!\n")
    return 1



array = []
generateList(array, random.randint(10, 50), 0, 2000)
print (array)
insertionSort(array)
print(array)
check(array)

array = []
generateList(array, random.randint(10, 50), 0, 2000)
print (array)
bubbleSort(array)
print(array)
check(array)

array = []
generateList(array, random.randint(10, 50), 0, 2000)
print (array)
selectionSort(array)
print(array)
check(array)

array = []
generateList(array, random.randint(10, 50), 0, 2000)
print (array)
quickSort(array)
print(array)
check(array)
