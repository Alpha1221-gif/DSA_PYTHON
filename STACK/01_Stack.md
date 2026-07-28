# 🐍 Stacks

A concise guide to understanding, optimizing, and implementing the Last In, First Out (LIFO) Stack data structure in Python 3.

---

## 🧭 Core Concepts

* **Definition:** A linear data structure holding multiple elements where the last element added is always the first one removed.
* **Analogy:** Like a pile of pancakes, elements are both added and removed exclusively from the top.
* **LIFO Mechanism:** This organizational system is known as **LIFO** (Last In, First Out).

---

## 📊 Basic Stack Operations

| Operation | Action | Time Complexity |
| :--- | :--- | :--- |
| **Push** | Adds a new element to the top of the stack | \(O(1)\) |
| **Pop** | Removes and returns the top element from the stack | \(O(1)\) |
| **Peek** | Returns the top (last) element without removing it | \(O(1)\) |
| **isEmpty**| Checks if the stack contains zero elements | \(O(1)\) |
| **Size** | Finds the total number of elements in the stack | \(O(1)\) |

> 💡 **Implementation Note:** Stacks can be structurally implemented using either **Arrays** (Python lists) or **Linked Lists**.

---

## 💻 Python Blueprint Implementation

```python
class Stack:
    def __init__(self):
        """Initialize an empty stack using a dynamic array (list)."""
        self._stack = []

    def push(self, item):
        """Adds a new element onto the stack."""
        self._stack.append(item)

    def pop(self):
        """Removes and returns the top element from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._stack.pop()

    def peek(self):
        """Returns the top (last) element on the stack."""
        if self.is_empty():
            return None
        return self._stack[-1]

    def is_empty(self) -> bool:
        """Checks if the stack is empty."""
        return len(self._stack) == 0

    def size(self) -> int:
        """Finds the number of elements in the stack."""
        return len(self._stack)

if __name__ == "__main__":
    pancakes = Stack()
    pancakes.push("Pancake 1")
    pancakes.push("Pancake 2")
    
    print(f"Top pancake (Peek): {pancakes.peek()}")
    print(f"Removed: {pancakes.pop()}")
    print(f"Remaining Size: {pancakes.size()}")
```

---

## 🎯 High-Yield Interview Targets

1. 🟩 **Valid Parentheses** – Matching brackets using character stacks
2. 🟨 **Evaluate Reverse Polish Notation** – Postfix math string parsing
3. 🟨 **Min Stack** – Retrieving the minimum element in constant \(O(1)\) time

---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```
