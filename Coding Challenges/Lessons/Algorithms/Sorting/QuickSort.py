## If no additional structures are allowed, perhaps we can sort the string and simply compare each character with the one next to it.
## O(N log N)


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first < last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist, splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

alist = [3, 2, 3, 45, 2, 12, 2, 0, 22, 3, 5, 6, 23, 5, 46, 2, 61, 7, 8, 3]
quickSort(alist)
print(alist)


Aarray = [3, 2, 3, 45, 2, 12, 2, 0, 22, 3, 5, 6, 23, 5, 46, 2, 61, 7, 8, 3]
