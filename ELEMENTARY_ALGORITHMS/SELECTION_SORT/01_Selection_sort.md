# 🐍 Selection Sort in Python

An interactive guide and implementation of the **Selection Sort** algorithm.

---

## 💻 Python Implementation

```python
def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

# Example Usage
if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print(f"Original Array: {data}")
    print(f"Sorted Array:   {selection_sort(data)}")
```

---

## ⏱️ Time & Space Complexity

* 🔴 **Worst-Case Time Complexity:** $O(n^2)$ — Occurs when the input array is sorted in reverse order.
* 🟡 **Average Time Complexity:** $O(n^2)$ — Occurs on a randomly shuffled array.
* 🔴 **Best-Case Time Complexity:** $O(n^2)$ — Unlike Bubble Sort, it still scans the remaining array even if it is already sorted.
* 🔵 **Space Complexity:** $O(1)$ — Requires a constant amount of additional memory space (In-place sorting).

---

## 🛠️ Where is it Used?

While Selection Sort is not ideal for large datasets due to its rigid $O(n^2)$ time complexity, it has distinct advantages in specific scenarios:

* 📚 **Teaching Core Concepts:** Perfect for introducing the mechanical logic of scanning, finding a minimum value, and performing controlled swaps.
* ⚡ **Minimizing Memory Swaps:** It performs a maximum of $O(n)$ swaps. This makes it highly valuable when writing to memory is extremely expensive or wears out the hardware (like Flash memory / EEPROM).
* 💾 **Systems with Limited Memory:** Operates completely in-place with $O(1)$ auxiliary space, making it perfect for tiny auxiliary systems.
* 🔍 **Small Datasets:** Performs efficiently on small lists where the overhead of more complex algorithms (like Quick Sort) is unnecessary.

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
