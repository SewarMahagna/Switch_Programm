#Open Addressing (Linear Probing)
class HashTable:
    def __init__(self,dic_size):
        self.dic_size=dic_size
        self.arr_table = [None] * self.dic_size

    def hash_function(self, key):
        return key % self.dic_size
    
    def get(self, key):
        return self.arr_table[self.hash_function(key)]

    def set(self, key, value):
        original_index = self.hash_function(key)
        new_index = original_index
        while self.arr_table[new_index] is not None :
            new_index = self.hash_function(new_index+1)
            if new_index == original_index : 
                raise Exception("Hash table is full!")
        self.arr_table[new_index]=value

    

# Example usage
table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: good (because 123 overwrote the value at index 3)
print(table.get(5251))  # Output: world
print(table.get(22))    # Output: None (no value at 22 % 5 = 2)