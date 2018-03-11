#HashTable

class objectData:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.point = None

class HashTable:
    def __init__(self, size):
        self.hashSize = size
        self.hashTable = []
        empty = objectData(None, None)
        for i in range(self.hashSize):
            self.hashTable.append(empty)


    def hashFunction(self, key):
        asciiTotal = 0
        for letter in key:
            asciiTotal = asciiTotal + ord(letter)
        hashKey = asciiTotal % self.hashSize
        return hashKey


    def hashStore(self, objectData):
        hashkey = self.hashFunction(objectData.key)
        if (self.hashTable[hashkey].key == None):
            self.hashTable[hashkey] = objectData
            print("[INFO] Data Stored at " + str(hashkey))
            return 1
        elif (self.hashTable[hashkey].key == objectData.key):
            print("[WARNING] That Key Already Exists.")
            return 0
        else:
            chain = self.hashTable[hashkey]
            while (chain.point != None):
                if (chain.point.key == objectData.key):
                    print("[WARNING] That Key Already Exists.")
                    return 0
                else:
                    chain = chain.point
            chain.point = objectData
            print("[INFO] Data Stored at " + str(hashkey) + " in a Chain.")
            return chain.point


    def hashEdit(self, key, data):
        hashkey = self.hashFunction(key)
        if (self.hashTable[hashkey].key == None):
            print("[WARNING] Data Does Not Exist")
            return 0
        elif (self.hashTable[hashkey].key == key):
            self.hashTable[hashkey].data = data
            print("[INFO] Data of [" + str(key) + "] has been edited.")
            return 1
        else:
            chain = self.hashTable[hashkey]
            while (chain.point != None):
                if (chain.point.key == key):
                    chain.point.data = data
                    print("[INFO] Data of [" + str(key) + "] has been edited across the Chain.")
                    return 1
                else:
                    chain = chain.point
            print("[WARNING] Data Does Not Exist")
            return 0

    def hashGet(self, key):
        hashkey = self.hashFunction(key)
        if (self.hashTable[hashkey].key == None):
            print("[WARNING] Data Does Not Exist")
            return 0
        elif (self.hashTable[hashkey].key == key):
            return self.hashTable[hashkey].data
        else:
            chain = self.hashTable[hashkey]
            while (chain.point != None):
                if (chain.point.key == key):
                    return chain.point.data
                else:
                    chain = chain.point
            print("[WARNING] Data Does Not Exist")
            return 0
