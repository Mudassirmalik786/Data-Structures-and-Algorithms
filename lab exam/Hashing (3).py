class MyHashTable:
    def __init__(self, hsize):
        self.size = hsize
        self.table = [None] * hsize
        self.numKeys = 0

    def getHash(self, key):     
        hashValue = 0
        for char in str(key):
            hashValue += ord(char)
        return hashValue % self.size

    def getTableSize(self):
        return self.size

    def getNumofKeys(self):
        return self.numKeys

    def rehash(self): 
        newSize = self.size * 2
        newTable = [None] * newSize
        for i in self.table:
            if i is not None:
                key, value = i
                newHash = self.getHash(key)
                newTable[newHash] = (key, value)
        self.table = newTable
        self.size = newSize

    def updateKey(self, key, value):
        hashValue = self.getHash(key)
        if self.table[hashValue] is None:      
            self.table[hashValue] = (key, value)
            self.numKeys += 1
        else:
            self.table[hashValue] = (key, value)
        if self.numKeys / self.size > 0.75:
            self.rehash()

    def searchKey(self, key):
        hashValue = self.getHash(key)
        if self.table[hashValue] is not None and self.table[hashValue][0] == key:
            return self.table[hashValue][1]
        else:
            return None

class WordCounter:
    def __init__(self, size):
        self.hashTablee = MyHashTable(size)

    def countWords(self, text):
        words = text.split()
        for word in words:
            word = word.lower() 
            count = self.hashTablee.searchKey(word)
            if count is None:
                self.hashTablee.updateKey(word, 1)
            else:
                self.hashTablee.updateKey(word, count + 1)

    def printWordCounts(self):
        for item in self.hashTablee.table:
            if item is not None:
                key, value = item
                print(f"{key}: {value}")


# Output:
text = "My Name is zohaib"
word_counter = WordCounter(10) 
word_counter.countWords(text)
word_counter.printWordCounts()
