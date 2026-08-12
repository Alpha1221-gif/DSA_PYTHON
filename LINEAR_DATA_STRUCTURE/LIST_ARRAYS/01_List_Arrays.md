# 🐍 Python DSA Dashboard: Arrays & Lists 🚀

Welcome to your beginner-friendly learning hub for Data Structures and Algorithms (DSA). Use this file to track your progress, practice concepts, and master the fundamentals!

---

### 📊 Master Progress Checklist 
* [ ] 🧊 **Array Basics** — Memory layout & 0-based indexing
* [ ] 🗂️ **Python Lists** — Dynamic sizing and common operations
* [ ] 🔍 **Searching** — Linear Search & Binary Search
* [ ] 🧮 **Sorting** — Bubble Sort & Selection Sort
* [ ] 🧠 **Two-Pointer Technique** — Reversing arrays, checking palindromes
* [ ] 🪟 **Sliding Window** — Fixed-size subarray problems

---

### 🧩 Core Concepts

#### 1️⃣ Arrays 🧱
* Fixed-size data structures that store elements of the same type in consecutive memory locations.
* **Fast access**: You can read any element instantly using its index O(1).
* **Slow changes**: Inserting or deleting an element requires shifting other items O(N).

#### 2️⃣ Python Lists 🛒
* Python does not have a traditional built-in "array". Instead, it uses **Lists**.
* Lists are **Dynamic Arrays**—they automatically resize themselves when they run out of space.
* They are flexible and can hold different data types together (e.g., `["Python", 3, True]`).

---

### 💻 Code Playground

#### Example: Reversing a List (Two-Pointer Technique) 🔄
This is a classic beginner DSA pattern. We place one pointer at the start and one at the end, swapping them until they meet in the middle.

```python
def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements using Python's clean unpacking syntax
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
        
    return arr

# Test the function
my_list = [10, 20, 30, 40, 50]
print(f"Original List: {my_list}")
print(f"Reversed List: {reverse_list(my_list)}")
```

---

### 🛠️ Python List Cheat Sheet

| Operation | Syntax | Time Complexity | What it does |
| :--- | :--- | :--- | :--- |
| **Access** | `my_list[i]` | O(1) | Gets the item at index `i` |
| **Append** | `my_list.append(x)` | O(1) | Adds item `x` to the very end |
| **Insert** | `my_list.insert(i, x)` | O(N) | Inserts item `x` at index `i` |
| **Remove** | `my_list.remove(x)` | O(N) | Removes the first occurrence of item `x` |
| **Pop** | `my_list.pop()` | O(1) | Removes and returns the last item |
| **Length** | `len(my_list)` | O(1) | Returns total number of elements |

---

### 💡 Beginner Tips
* **Index Errors**: Always remember that indexing starts at `0`. The last item is at index `len(my_list) - 1`.
* **Negative Indexing**: Python lets you count backwards! `my_list[-1]` gives you the very last item.

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```
