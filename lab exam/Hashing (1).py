class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:
    def __init__(self,size=10):
        self.size = size
        self.array = [None] * size
        self.keys_occupied = 0

    def hashFunction(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hashFunction(key)
        new_node = KeyNode(key, value)

        if self.array[index] is None:
            self.array[index] = new_node
        else:
            # collision check
            current = self.array[index]
            while current.next:
                current = current.next
            current.next = new_node

        self.keys_occupied += 1

    def delete(self, key):
        index = self.hashFunction(key)
        current = self.array[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.array[index] = current.next
                self.keys_occupied -= 1
                return True  

            prev, current = current, current.next

        return False  

    def retrieve(self, key):
        index = self.hashFunction(key)
        current = self.array[index]

        while current:
            if current.key == key:
                return current.value 
            current = current.next

        return None  

# Output:
myHashTable = MyHashTable()

myHashTable.insert("one", 1)
myHashTable.insert("two", 2)
myHashTable.insert("three", 3)
print(myHashTable.retrieve("one")) 
print(myHashTable.keys_occupied) 
myHashTable.delete("two")
print(myHashTable.retrieve("two"))
print(myHashTable.keys_occupied)
