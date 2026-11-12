# 🐍 Hash Tables in Python 🗂️

A **Hash Table** (implemented as a `dict` or `set` in Python) is a powerful data structure that stores data in an associative manner using **key-value pairs** (`Key ➔ Value`). It uses a mathematical **hash function** to compute an index into an array of buckets, allowing for ultra-fast data retrieval.

---

## 🧠 Core Concepts

* 🔑 **Key-Value Pairs:** Data is stored by mapping a unique, immutable **key** (like a string, integer, or tuple) to a specific **value**.
* ⚙️ **Hash Function:** A built-in function (`hash()`) that converts a key into a fixed-size integer (the hash code) to determine the exact memory index where the value is stored.
* 💥 **Collisions:** Occurs when two different keys produce the exact same hash index. Common ways to resolve this include **Chaining** (storing a list of items at the same index) and **Open Addressing** (probing for the next empty slot).
* 📈 **Load Factor & Resizing:** When the table gets too full (usually around `2/3` capacity in Python), it automatically resizes to a larger array and re-hashes existing keys to maintain speed.

---

## 💻 1. Built-in Hash Table (`dict`) in Python

Python's built-in dictionary (`dict`) is a highly optimized hash table.

```python
# 1️⃣ Creating a Hash Table (Dictionary)
student_scores = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92
}

# 2️⃣ Inserting / Updating a Key-Value Pair ➔ O(1)
student_scores["David"] = 90
student_scores["Alice"] = 98  # Updates existing key

# 3️⃣ Accessing a Value by Key ➔ O(1)
print(student_scores["Bob"])          # Output: 88
print(student_scores.get("Eve", 0))   # Safe lookup, Output: 0

# 4️⃣ Checking if a Key Exists ➔ O(1)
if "Charlie" in student_scores:
    print("Charlie is in the table! ✅")

# 5️⃣ Deleting a Key-Value Pair ➔ O(1)
del student_scores["Bob"]
```

---

## 🛠️ 2. Building a Custom Hash Table from Scratch (Using Chaining)

Here is how a Hash Table works under the hood using Python lists and **Separate Chaining** to handle collisions:

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Create a list of empty buckets (lists) for chaining
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        # Compute a valid index within the table size
        return hash(key) % self.size

    # ➕ Insert or Update ➔ Average O(1)
    def insert(self, key, value):
        index = self._hash_function(key)
        bucket = self.table[index]

        # Update value if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Otherwise, append new key-value pair
        bucket.append((key, value))

    # 🔍 Search / Get ➔ Average O(1)
    def get(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    # ❌ Delete ➔ Average O(1)
    def delete(self, key):
        index = self._hash_function(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

# 🧪 Example Usage
ht = HashTable()
ht.insert("apple", 100)
ht.insert("banana", 200)
ht.insert("orange", 300)

print("Apple price:", ht.get("apple"))   # Output: 100
ht.delete("banana")
print("Banana price:", ht.get("banana")) # Output: None
```

---

## ⏱️ Time & Space Complexity

| Operation | Average Case | Worst Case ⚠️ | Notes |
| :--- | :---: | :---: | :--- |
| **🔍 Search / Lookup** | `O(1)` | `O(n)` | Instant access via hash index |
| **➕ Insertion** | `O(1)` | `O(n)` | Worst case occurs during table resizing |
| **❌ Deletion** | `O(1)` | `O(n)` | Worst case occurs with heavy hash collisions |
| **💾 Space Complexity** | `O(n)` | `O(n)` | Scales linearly with the number of elements |

> 💡 **Note:** The `O(n)` worst-case time complexity happens only if a poor hash function causes every key to collide into the exact same bucket, turning the lookup into a linear search.

---

## 🌍 Real-World Applications

* 🗄️ **Database Indexing:** Databases use hash indexes to locate records on disk immediately without scanning entire tables.
* ⚡ **Caching Systems:** Tools like Redis and browser caches store frequently accessed web pages or API responses for instant retrieval.
* 🔐 **Password Verification:** Websites store cryptographic hashes of passwords rather than plain text to verify logins securely.
* 🧬 **Counting & Deduplication:** Quickly finding duplicate items in a dataset or counting word frequencies (e.g., using Python's `collections.Counter`).
* 🌐 **DNS Resolution:** Mapping human-readable domain names (like `google.com`) to their corresponding IP addresses.

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
