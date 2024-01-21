class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash_function1(self, key):
        return key % self.size

    def hash_function2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        index = self.hash_function1(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = key
        else:
            i = 1
            while True:
                new_index = (index + i * self.hash_function2(key)) % self.size
                if self.hash_table[new_index] is None:
                    self.hash_table[new_index] = key
                    break
                i += 1

    def search(self, key):
        index = self.hash_function1(key)
        if self.hash_table[index] == key:
            return index
        else:
            i = 1
            while True:
                new_index = (index + i * self.hash_function2(key)) % self.size
                if self.hash_table[new_index] == key:
                    return new_index
                elif self.hash_table[new_index] is None:
                    return -1
                i += 1

def main():
    hash_table = DoubleHashing(10)
    hash_table.insert(5)
    hash_table.insert(15)
    hash_table.insert(25)
    hash_table.insert(35)

    print(hash_table.search(15))  # Output: 2
    print(hash_table.search(25))  # Output: 3
    print(hash_table.search(35))  # Output: 4
    print(hash_table.search(45))  # Output: -1

if __name__ == "__main__":
    main()
