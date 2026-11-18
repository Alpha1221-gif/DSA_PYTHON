# -//- ----  CODE# -//- ----  #

class hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Flat array with no linked lists

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        # Loop through the array to find an empty slot or matching key
        for _ in range(self.size):
            # If slot is empty, insert the key-value tuple here
            if self.table[index] is None:
                self.table[index] = (key, value)
                return

            # If key already exists, update its value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            # Collision happened! Move to the next slot (wrap around if at the end)
            index = (index + 1) % self.size

        print("Error: Hash table is full!")

    def get(self, key):
        index = self._hash(key)

        # Search starting from the hashed index
        for _ in range(self.size):
            # If we hit an empty slot, the key is not in the table
            if self.table[index] is None:
                return None

            # If we find the matching key, return its value
            if self.table[index][0] == key:
                return self.table[index][1]

            # Check the next slot
            index = (index + 1) % self.size

        return None  # Key not found


# --- Example Usage ---
ht = hashtable(5)

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("cherry", 30)

print(ht.get("banana"))  # Output: 20
print(ht.table)  # Shows the flat array with (key, value) tuples
