# 🐍 Insertion Sort in Python (DSA)

**Insertion Sort** is a straightforward, intuitive sorting algorithm that works similarly to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

---

## 💻 Python Code Implementation

```python
def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr

# Example Usage:
if __name__ == "__main__":
    data = [9, 5, 1, 4, 3]
    print("Original Array: ", data)
    
    sorted_data = insertion_sort(data)
    print("Sorted Array:   ", sorted_data)
```

---

## 📊 Complexity Analysis

* **Time Complexity:**
  * 🟢 **Best Case:** $O(n)$ — Occurs when the array is **already sorted**. The inner `while` loop condition fails immediately every time.
  * 🟡 **Average Case:** $O(n^2)$ — Occurs when elements are randomly distributed.
  * 🔴 **Worst Case:** $O(n^2)$ — Occurs when the array is **sorted in reverse order**. Every element must be shifted across the entire sorted sub-array.
* **Space Complexity:**
  * 💾 **Auxiliary Space:** $O(1)$ — It is an **in-place** sorting algorithm; it requires no extra memory allocation.

---

## 🌍 Real-Life Applications

* ⚙️ **Hybrid Sorting (Timsort & IntroSort):** Standard library sort functions (like Python’s `sort()`) use hybrid algorithms. They use Merge or Quick Sort for massive inputs, but switch to **Insertion Sort for small arrays (under 64 elements)** due to its ultra-low overhead.
* 📶 **Online/Streaming Data:** If you receive numbers one by one (like live stock tickers), Insertion Sort inserts the new item into a pre-sorted list in quick $O(n)$ time.
* 🧹 **Nearly Sorted Lists:** If a list is already mostly sorted (with just a few misplaced elements), Insertion Sort cleans it up faster than advanced algorithms.
