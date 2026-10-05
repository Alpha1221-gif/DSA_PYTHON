# 🐍 Stack Data Structure in Python

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added to the stack is the first one to be removed. Think of it like a stack of plates; you can only add or remove plates from the top.

---

## 🛑 Time & Space Complexity

| Operation | Time Complexity | Space Complexity | Description |
| :--- | :--- | :--- | :--- |
| **Push** | O(1) | O(1) | Adds an item to the top of the stack. |
| **Pop** | O(1) | O(1) | Removes and returns the top item. |
| **Peek / Top** | O(1) | O(1) | Returns the top item without removing it. |
| **Is Empty** | O(1) | O(1) | Checks if the stack has no elements. |
| **Size** | O(1) | O(1) | Returns the total number of elements. |

---

## 🛠️ Python Implementation

This implementation uses a standard Python list to store elements, making it simple, readable, and easy to understand.

```python
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the top item if the stack is not empty
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        # Return True if stack has no elements, else False
        return len(self.stack) == 0

    def size(self):
        # Return the total number of elements in the stack
        return len(self.stack)


# --- Demonstration of Usage ---
if __name__ == "__main__":
    my_stack = Stack()

    # Pushing elements
    print("Pushing elements...")
    my_stack.push("google.com")
    my_stack.push("github.com")
    my_stack.push("stackoverflow.com")

    # Check the top element
    print("Top element (Peek):", my_stack.peek())

    # Popping elements
    print("Popped item:", my_stack.pop())
    print("Popped item:", my_stack.pop())

    # Check current state
    print("Current Stack Size:", my_stack.size())
    print("Is Stack Empty?", my_stack.is_empty())
```

---

## 🎯 Common Interview Patterns & LeetCode Applications

Stacks are highly utilized across many computational problems. Look out for these patterns:

*   **Balanced Parentheses / Bracket Matching:** Using a stack to match opening brackets with corresponding closing brackets (e.g., LeetCode 20: *Valid Parentheses*).
*   **Monotonic Stack:** Keeping stack elements strictly increasing or decreasing to find the next greater or smaller element (e.g., LeetCode 739: *Daily Temperatures*).
*   **Expression Evaluation / Parsing:** Converting or parsing infix expressions to postfix/prefix formats (e.g., LeetCode 224: *Basic Calculator*).
*   **Backtracking & History Management:** Simulating undo/redo features or deep directory traversals (e.g., DFS algorithm).


---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```
