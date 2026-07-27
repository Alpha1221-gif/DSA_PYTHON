# 🐍 Arrays and Lists

A concise guide to understanding, optimizing, and implementing sequential linear data structures in Python 3.

---

## 🧭 Core Concepts

* **Low-Level Array:** Contiguous memory blocks storing items of the same data type. Provides instantaneous \(O(1)\) index access.
* **Python List:** A dynamic array tracking pointers to objects. Handles resizing and mixed data types automatically.

---

## 📊 Complexity Matrix

| Operation | Time Complexity | Structural Impact |
| :--- | :--- | :--- |
| **Access by Index** | \(O(1)\) | Direct memory address calculation |
| **Search by Value** | \(O(n)\) | Requires a sequential sweep |
| **Insertion at End** | \(O(1)\) amortized | Fast, unless array reallocation triggers |
| **Insert/Delete (Mid)**| \(O(n)\) | Forces elements to shift left or right |

---

## 🛠️ Optimization Patterns

* ↔️ **Two-Pointer Strategy:** Two index variables moving toward each other or at different speeds to solve array variations in \(O(n)\) time.
* 🪟 **Sliding Window:** Maintaining a sub-array frame that dynamically expands or contracts to track running sequential constraints.
* ➕ **Prefix Sums:** Pre-computing running totals to answer range sum queries in instant \(O(1)\) time.

---

## 💻 Python Blueprint Implementation

```python
class ArrayOptimizations:
    @staticmethod
    def reverse_array(arr: list) -> list:
        """Reverses an array in-place using two pointers."""
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left + 1, right - 1
        return arr

    @staticmethod
    def max_window_sum(arr: list, k: int) -> int:
        """Finds max sum of K consecutive elements using sliding window."""
        if len(arr) < k: return 0
        window_sum = sum(arr[:k])
        max_sum = window_sum
        for i in range(len(arr) - k):
            window_sum = window_sum - arr[i] + arr[i + k]
            max_sum = max(max_sum, window_sum)
        return max_sum

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(f"Reversed: {ArrayOptimizations.reverse_array(nums.copy())}")
    print(f"Max Sum (K=3): {ArrayOptimizations.max_window_sum([2, 1, 5, 1, 3, 2], 3)}")
```

---

## 🎯 High-Yield Interview Targets

1. 🟩 **Two Sum** – Array mapping via hashing
2. 🟨 **Container With Most Water** – Two-pointer boundary restriction
3. 🟨 **Maximum Subarray (Kadane’s)** – $O(n)$ dynamic running computation

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```
