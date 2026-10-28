# 🐍 Binary Search in Python

**Binary search is an efficient algorithm used to find the position of a target value within a sorted array.** Unlike a linear search that checks every element sequentially, binary search repeatedly divides the search interval in half.

## 💻 Python Implementation

Here is a standard iterative implementation of the binary search algorithm:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        
        # If target is smaller, ignore right half
        else:
            high = mid - 1
            
    # Element was not present in the array
    return -1

# Example usage:
sorted_list = [2, 3, 4, 10, 40]
target_value = 10

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")
```

---

## 🎯 What it is Used For & Where it is Used

### Core Use Case
Binary search is used to **quickly locate items in large, sorted datasets** where a sequential scan would be too slow. 

### Real-World Applications
* **Database Indexing:** Databases use binary search mechanisms (like B-Trees) to retrieve records rapidly without scanning the entire database.
* **Dictionary Lookups:** Finding a word in a digital dictionary or a name in a contact list.
* **Debugging (Git Bisect):** Developers use binary search to look through commit histories to find exactly which commit introduced a bug.
* **Library Functions:** Built-in programming tools like Python's `bisect` module, Java’s `Arrays.binarySearch()`, and C++’s `std::binary_search` rely on this logic.

---

## ⏱️ Complexity Analysis

### Time Complexity
* **Best Case: $O(1)$** — The target element is exactly in the middle of the array on the very first check.
* **Average Case: $O(\log n)$** — The search space is cut in half with each step.
* **Worst Case: $O(\log n)$** — The target is at the far ends of the array, or not present at all.

### Space Complexity
* **Iterative Approach: $O(1)$** — The iterative version (shown above) uses a fixed number of variables (`low`, `high`, `mid`) regardless of the array size, requiring constant extra space.
* *(Note: A recursive implementation would require $O(\log n)$ space due to the call stack).*
