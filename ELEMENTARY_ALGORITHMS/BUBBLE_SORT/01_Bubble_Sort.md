# 🐍 Bubble Sort (Bubble Shot) in Python

An interactive guide and implementation of the **Bubble Sort** algorithm.

---

## 💻 Python Implementation

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, array is already sorted
        if not swapped:
            break
    return arr

# Example Usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original Array: {data}")
    print(f"Sorted Array:   {bubble_sort(data)}")
```

---

## ⏱️ Time & Space Complexity

* 🔴 **Worst-Case Time Complexity:** $O(n^2)$ — Occurs when the input array is sorted in reverse order.
* 🟡 **Average Time Complexity:** $O(n^2)$ — Occurs on a randomly shuffled array.
* 🟢 **Best-Case Time Complexity:** $O(n)$ — Occurs when the array is already sorted (optimized by checking the `swapped` flag).
* 🔵 **Space Complexity:** $O(1)$ — Requires a constant amount of additional memory space (In-place sorting).

---

## 🛠️ Where is it Used?

While Bubble Sort is rarely used in production applications due to its $O(n^2)$ efficiency on large datasets, it is highly valuable in specific scenarios:

* 📚 **Educational Purposes:** It serves as a fundamental concept to introduce students to the logic of sorting algorithms and algorithmic thinking.
* 🏎️ **Nearly Sorted Data:** It is highly efficient for data collections that are already almost sorted, requiring only a few checks.
* 💾 **Memory-Constrained Systems:** Useful in small, embedded systems where memory overhead must be minimized ($O(1)$ space).
* 🔒 **Computer Graphics:** Used in graphics processing pipelines to detect tiny out-of-order anomalies (like polygon sorting) where objects shift only slightly between frames.

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
