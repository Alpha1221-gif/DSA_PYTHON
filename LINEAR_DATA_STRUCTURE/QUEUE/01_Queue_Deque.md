# 🐍 Data Structures in Python: Queue & Deque

This repository contains clean, efficient Python implementations of **Queues** and **Deques (Double-Ended Queues)** using built-in lists, `collections.deque`, and singly linked lists.

---

## 📥 1. Queue Implementation

A Queue follows the **FIFO (First In, First Out)** principle. Elements are inserted at the back (enqueue) and removed from the front (dequeue).

### ⚙️ Using `collections.deque` (Recommended)
Python's built-in `deque` is optimized for fast O(1) appends and pops from both ends.

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.popleft()

    def peek(self):
        """Return the item at the front without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.queue)

    def __str__(self):
        return f"Queue: {list(self.queue)}"


# Example Usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print(q)          # Output: Queue: [10, 20, 30]
    print(q.dequeue()) # Output: 10
    print(q.peek())    # Output: 20
    print(q.size())    # Output: 2
```

---

## 🔄 2. Deque Implementation

A Deque (Double-Ended Queue) allows you to insert and remove elements from **both the front and the back** with equal efficiency.

### ⚙️ Custom Deque wrapper using `collections.deque`

```python
from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return len(self.deque) == 0

    def add_front(self, item):
        """Add an item to the front of the deque."""
        self.deque.appendleft(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque."""
        self.deque.append(item)

    def remove_front(self):
        """Remove and return the item from the front."""
        if self.is_empty():
            raise IndexError("Remove from an empty deque")
        return self.deque.popleft()

    def remove_rear(self):
        """Remove and return the item from the rear."""
        if self.is_empty():
            raise IndexError("Remove from an empty deque")
        return self.deque.pop()

    def peek_front(self):
        """Get the front item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty deque")
        return self.deque[0]

    def peek_rear(self):
        """Get the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty deque")
        return self.deque[-1]

    def size(self) -> int:
        """Return the total number of items."""
        return len(self.deque)

    def __str__(self):
        return f"Deque: {list(self.deque)}"


# Example Usage:
if __name__ == "__main__":
    d = Deque()
    d.add_rear(5)
    d.add_rear(10)
    d.add_front(1)
    
    print(d)               # Output: Deque: [1, 5, 10]
    print(d.remove_rear()) # Output: 10
    print(d.remove_front())# Output: 1
    print(d)               # Output: Deque: [5]
```

---

## 📊 3. Time Complexity Summary

| 🛠️ Operation | 📥 Queue (`deque`) | 🔄 Deque (`deque`) | 🐍 Python Standard List (`list`) |
| :--- | :--- | :--- | :--- |
| **Insert Front** / `appendleft` | N/A | **O(1)** | O(n) |
| **Insert Rear** / `append` | **O(1)** | **O(1)** | O(1) amortized |
| **Delete Front** / `popleft` | **O(1)** | **O(1)** | O(n) |
| **Delete Rear** / `pop` | N/A | **O(1)** | O(1) |

