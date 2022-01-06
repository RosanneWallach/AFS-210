class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        return key % self.size

    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self,key,data):
        # Insert your code here to store key and data 
        idx = self.hashfunction(key)
        if self.slots[idx] != None:
            idx = self.rehash(key)
        self.slots[idx] = key
        self.data[idx] = data

    def get(self,key):
        # Insert your code here to get data by key
        idx = self.hashfunction(key)
        if self.slots[idx] != key:
            idx = self.rehash(key)
        return self.data[idx]

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A' # setitem
# Store remaining input data
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H[52]) # getitem

