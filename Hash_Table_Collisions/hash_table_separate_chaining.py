#Separate Chaining
class HashTable:
    def __init__(self,dic_size):
        self.dic_size=dic_size
        self.arr_table = [[] for _ in range(dic_size)]

    def hash_function(self, key):
        return key % self.dic_size
    
    def get(self, key):
        index = self.hash_function(key)
        linked_list = self.arr_table[index]
        for lst in linked_list : 
            if lst[0]== key : 
                return lst[1]
            
        return None

    def set(self, key, value):
        index = self.hash_function(key)
        linked_list = self.arr_table[index]

        for lst in linked_list:
            if lst[0]== key:
                lst[1]= value
                print("Key Collision :  The value updated!")
                return
        linked_list.append([key,value]) 
# Example usage
table = HashTable(5)
table.set(238, "hello")  # 238 % 5 = 3
table.set(5251, "world")  # 5251 % 5 = 1
table.set(123, "good")  # 123 % 5 = 3 (collision with 238)

# Retrieving values
print(table.get(238))   # Output: good (because 123 overwrote the value at index 3)
print(table.get(5251))  # Output: world
print(table.get(22))    # Output: None (no value at 22 % 5 = 2)
print(table.get(123))    # Output: None (no value at 22 % 5 = 2)


