# 🐍 Linear Search in Python

**Linear search is a sequential algorithm that checks every element in a list one by one until it finds the target value or reaches the end.** It is the simplest searching method and requires no prior sorting of the data.

---

## 💻 Python Implementation

```python
def linear_search(arr, target):
    """
    Performs a linear search on a list to find a target element.
    
    Parameters:
    arr (list): The list of elements to search through.
    target: The element to find.
    
    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Target found, return its index
            
    return -1  # Target not found in the list

# --- Example Usage ---
if __name__ == "__main__":
    numbers = [4, 2, 9, 7, 1, 5]
    target_value = 7
    
    result = linear_search(numbers, target_value)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")
```

---

## 🛠️ Uses & Applications

### Where it is used
* **Unsorted Data:** When the dataset is completely unsorted and you cannot use faster algorithms like binary search.
* **Small Datasets:** When the number of elements is small, making the overhead of sorting the data or building complex structures inefficient.
* **Simple Data Structures:** Ideal for single linked lists or streams of incoming data where random access is not possible.

### How it is used
* **Checking Presence:** Verifying if an item (like a username or an ID number) exists in a small configuration file or list.
* **Finding First Occurrence:** Locating the very first instance of a specific item in a collection.

---

## 📊 Complexity Analysis

### Time Complexity
* **Best Case: $O(1)$** 
  * Occurs when the target element is at the very beginning (the first index) of the array.
* **Worst Case: $O(n)$** 
  * Occurs when the target element is at the very end of the array, or not present at all. The algorithm must check all $n$ elements.
* **Average Case: $O(n)$** 
  * On average, the target will be found somewhere in the middle, requiring $\frac{n}{2}$ comparisons.

### Space Complexity
* **Total Space: $O(1)$**
  * It operates as an **in-place algorithm**. It only requires a constant amount of extra memory for variables like the loop counter (`index`), regardless of how large the input array grows.

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```

