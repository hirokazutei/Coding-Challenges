# 3.1 Three in One
# Describe how you could use a single array to impement three stacks.

## The simplest solution is to divide the array into three like a nested array so that:
## array[n*3] is the first stack, array[n*3 + 1] is the second stack, and array[n*3 + 2] is the third stack.
## Process of append and pop: O(N)
## Memory: O(N) [the largest of the three stacks multiplied by 3]

class ListStack:
    def __init__(self):
        self.stackList = [60]
        self.startA = 0
        self.endA = 19
        self.startB = 20
        self.endB = 39
        self.startC = 40
        self.endC = 59

    def push(self, data):
        self.stackList.append(data)

    def pop(self):
        returnV = self.stackList[-1]
        self.stackList.pop()
        return returnV

    def peek(self):
        return self.stackList[-1]

    def isEmpty(self):
        if (self.stackList == []):
            return True
        return False


## The more space efficient solution is to use poiters to keep track of the beginning and end of the stack.
## While efficient in use of an array, the process of appending CAN be more expensive.
