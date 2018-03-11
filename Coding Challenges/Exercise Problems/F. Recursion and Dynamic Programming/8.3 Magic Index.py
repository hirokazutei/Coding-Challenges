# Magic Index
# A magic index in an array A[0... n-1] is defined to be an indexsuch that A[i] = i.
# Given a sorted array of distinct integers, write method to find a magic index, in array A.


class Index:
    def __init__(self, array):
        self.array = array

    def bruteForce(self):
        for i in range(len(self.array)):
            if i is self.array[i]:
                return i

    def binarySearch(self, begin = None, end = None):
        if begin is None:
            begin = 0
            end = len(self.array) - 1
            found = None
        pivot = end - begin //2
        if pivot is self.array[pivot]:
            return pivot
        elif pivot > self.array[pivot]:
            found = self.binarySearch(pivot + 1, end)
            if found is not None:
                return found
        elif pivot < self.array[pivot]:
            found = self.binarySearch(begin, pivot - 1)
            if found is not None:
                return found
        return False


i = Index([-1, 1, 3, 5, 8, 10, 13, 14, 15, 16, 18, 30])
print(i.binarySearch())