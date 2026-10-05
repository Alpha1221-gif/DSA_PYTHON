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

> **Note on Python Lists:** While Python lists can act as stacks using `.append()` and `.pop()`, they are dynamic arrays. When a list needs to resize, an occasional O(n) amortized cost occurs. For a strict O(1) guarantee, `collections.deque` is preferred.

---

## 🛠️ Python Implementation

This implementation uses `collections.deque` under the hood for optimal, thread-safe, and memory-efficient O(1) modifications from the top of the stack.

```python
from collections import deque
from typing import Any, Optional

class Stack:
    """A standard Object-Oriented implementation of a Stack using collections.deque."""

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._container: deque = deque()

    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self._container.append(item)

    def pop(self) -> Any:
        """Remove and return the top item from the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self._container.pop()

    def peek(self) -> Optional[Any]:
        """Return the top item without removing it. Returns None if empty."""
        if self.is_empty():
            return None
        return self._container[-1]

    def is_empty(self) -> bool:
        """Check if the stack contains no elements."""
        return len(self._container) == 0

    def size(self) -> int:
        """Return the number of elements currently in the stack."""
        return len(self._container)

    def __str__(self) -> str:
        """Provide a readable string representation of the stack state."""
        return f"Stack(bottom -> {list(self._container)} <- top)"


# --- Demonstration of Usage ---
if __name__ == "__main__":
    # 1. Initialize Stack
    history_stack = Stack()

    # 2. Push elements
    print("Pushing elements: 'google.com', 'github.com', 'stackoverflow.com'")
    history_stack.push("google.com")
    history_stack.push("github.com")
    history_stack.push("stackoverflow.com")
    print(history_stack)

    # 3. Peek top element
    print(f"Current Top (Peek): {history_stack.peek()}")

    # 4. Pop elements
    print(f"Popped item: {history_stack.pop()}")
    print(f"Popped item: {history_stack.pop()}")
    print(history_stack)

    # 5. Check size and empty status
    print(f"Stack size: {history_stack.size()}")
    print(f"Is stack empty? {history_stack.is_empty()}")
```

---

## 🎯 Common Interview Patterns & LeetCode Applications

Stacks are highly utilized across many computational problems. Look out for these patterns:

*   **Balanced Parentheses / Bracket Matching:** Using a stack to match opening brackets with corresponding closing brackets (e.g., LeetCode 20: *Valid Parentheses*).
*   **Monotonic Stack:** Keeping stack elements strictly increasing or decreasing to find the next greater or smaller element (e.g., LeetCode 739: *Daily Temperatures*).
*   **Expression Evaluation / Parsing:** Converting or parsing infix expressions to postfix/prefix formats (e.g., LeetCode 224: *Basic Calculator*).
*   **Backtracking & History Management:** Simulating undo/redo features or deep directory traversals (e.g., DFS algorithm).

