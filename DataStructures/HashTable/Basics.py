"""

    HashMaps are also dictionaries in python but we can also implement

"""

class HashTable:
    
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]
    
    def hashFunction(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.Max
    
    def add(self, key,value):
        add = self.hashFunction(key)
        self.arr[add] = value

    def get(self, key):
        return self.arr[self.hashFunction(key)]


hashTable1 = HashTable()
hashTable1.add("abhi",10) 
hashTable1.add("Nihar",20) 
hashTable1.add("nithin",30) 
print(hashTable1.get("Nihar"))