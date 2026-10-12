# 🐍 Data Structures in Python: Queue & Deque

This repository contains clean, beginner-friendly Python implementations of **Queues**, **Deques**, and **Circular Deques**, along with their real-world uses.

---

## 📥 1. Queue Implementation

A Queue follows the **FIFO (First In, First Out)** rule. The first item added is the first one removed (like a real-world waiting line).

### 💡 Real-World Uses
* **Printer Queues:** Managing documents sent to a printer.
* **Customer Support:** Handling support tickets or phone calls in the order they arrive.
* **Task Scheduling:** Operating systems running background jobs sequentially.

### ⚙️ Simple Code Example
```python
from collections import deque

class SimpleQueue:
    def __init__(self):
        # We use deque because it's super fast for adding/removing items
        self.items = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.items:
            return "Queue is empty!"
        return self.items.popleft()

    def peek(self):
        """See the item at the front without removing it."""
        if not self.items:
            return "Queue is empty!"
        return self.items[0]

    def size(self):
        """Get the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        return f"Queue: {list(self.items)}"


# Quick Test
if __name__ == "__main__":
    q = SimpleQueue()
    q.enqueue("Alice")
    q.enqueue("Bob")
    q.enqueue("Charlie")
    
    print(q)            # Output: Queue: ['Alice', 'Bob', 'Charlie']
    print(q.dequeue())  # Output: Alice
    print(q.peek())     # Output: Bob
```

---

## 🔄 2. Deque (Double-Ended Queue) Implementation

A Deque allows you to add and remove items from **both the front and the back** with equal speed.

### 💡 Real-World Uses
* **Browser History:** Going forward and backward through visited web pages.
* **Undo/Redo Actions:** Software tracking your edits from both ends.
* **Job Stealing Algorithms:** Multi-threaded systems balancing work items dynamically.

### ⚙️ Simple Code Example
```python
from collections import deque

class SimpleDeque:
    def __init__(self):
        self.items = deque()

    def add_front(self, item):
        """Add an item to the very front."""
        self.items.appendleft(item)

    def add_rear(self, item):
        """Add an item to the very back."""
        self.items.append(item)

    def remove_front(self):
        """Remove and return the front item."""
        if not self.items:
            return "Deque is empty!"
        return self.items.popleft()

    def remove_rear(self):
        """Remove and return the back item."""
        if not self.items:
            return "Deque is empty!"
        return self.items.pop()

    def __str__(self):
        return f"Deque: {list(self.items)}"


# Quick Test
if __name__ == "__main__":
    d = SimpleDeque()
    d.add_rear("Middle")
    d.add_front("First")
    d.add_rear("Last")
    
    print(d)                 # Output: Deque: ['First', 'Middle', 'Last']
    print(d.remove_rear())   # Output: Last
    print(d.remove_front())  # Output: First
```

---

## ⭕ 3. Circular Deque Implementation

A Circular Deque uses a fixed-size storage structure where the end connects back to the beginning. It avoids wasting memory slot positions as pointers shift.

### 💡 Real-World Uses
* **Media Player Playlists:** Creating a continuous "repeat all" loop for a set list of songs.
* **Traffic Light Timers:** Systems cycling through fixed states repeatedly.
* **Fixed-size Buffers:** Streaming audio/video data packets efficiently without dynamic memory resizing.

### ⚙️ Simple Code Example
```python
class SimpleCircularDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def insert_front(self, value):
        if self.size == self.capacity:
            return "Full!"
        # Move front pointer back circularly
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.items[self.front] = value
        self.size += 1
        return "Success"

    def insert_rear(self, value):
        if self.size == self.capacity:
            return "Full!"
        # Put item at rear, then move rear pointer forward circularly
        self.items[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return "Success"

    def delete_front(self):
        if self.size == 0:
            return "Empty!"
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return "Success"

    def delete_rear(self):
        if self.size == 0:
            return "Empty!"
        # Move rear pointer back circularly, then clear
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.items[self.rear] = None
        self.size -= 1
        return "Success"

    def __str__(self):
        return f"Buffer Array: {self.items} | Active Size: {self.size}/{self.capacity}"


# Quick Test
if __name__ == "__main__":
    cd = SimpleCircularDeque(3)
    print(cd.insert_rear("A"))   # Output: Success
    print(cd.insert_rear("B"))   # Output: Success
    print(cd.insert_front("C"))  # Output: Success
    print(cd.insert_rear("D"))   # Output: Full!
    print(cd)                    # Shows how the items sit inside the fixed array
```

---

## 📊 4. Time Complexity Cheat Sheet

| 🛠️ Operation | 📥 Queue (`deque`) | 🔄 Deque (`deque`) | ⭕ Circular Deque (Fixed List) |
| :--- | :--- | :--- | :--- |
| **Insert Front** | N/A | **O(1)** (Instant) | **O(1)** (Instant) |
| **Insert Rear** | **O(1)** (Instant) | **O(1)** (Instant) | **O(1)** (Instant) |
| **Delete Front** | **O(1)** (Instant) | **O(1)** (Instant) | **O(1)** (Instant) |
| **Delete Rear** | N/A | **O(1)** (Instant) | **O(1)** (Instant) |


---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```
