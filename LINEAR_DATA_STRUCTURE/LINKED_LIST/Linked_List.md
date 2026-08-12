# 🐍 Linked Lists Master Guide

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, elements are linked using pointers.

---

## 🟩 1. Singly Linked Lists
*Forward pointer traversals, node insertion, deletion, and sequence reversing techniques.*

### 🗺️ Visual Representation
`[Head] ➔ [Data | •➔] ➔ [Data | •➔] ➔ [Data | NULL]`

### ⚙️ Core Operations
* **Traversal:** Moving forward from the head to the end node.
* **Insertion:** Adding a node at the beginning, middle, or end.
* **Deletion:** Removing a target node and updating the pointer.
* **Reversal:** Flipping the pointer directions to reverse the sequence.

### ⏱️ Complexity Analysis
* **Access / Search:** O(n)
* **Insertion / Deletion (at Head):** O(1)
* **Insertion / Deletion (at Tail/Middle):** O(n)
* **Space Complexity:** O(n)

### 💻 Python Implementation
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
```

---

## 🟦 2. Doubly Linked Lists
*Forward and backward navigation nodes for efficient tracking.*

### 🗺️ Visual Representation
`[NULL] 🔁 [• ➔ Node 1 ➔ •] 🔁 [• ➔ Node 2 ➔ •] 🔁 [NULL]`

### ⚙️ Key Advantages
* **Bi-directional navigation:** Traversal is possible both forward and backward.
* **Easier deletion:** No need to track the previous node explicitly during removal.

### ⏱️ Complexity Analysis
* **Access / Search:** O(n)
* **Insertion / Deletion (with Node Pointer):** O(1)
* **Space Complexity:** O(n) *(Requires extra memory for back-pointers)*

### 💻 Python Implementation
```python
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = DLLNode(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
```

---

## 🟨 3. Circular Linked Lists
*Seamless ring-buffer node linking where the tail references the head node.*

### 🗺️ Visual Representation

```text
 ┌────────────────────────────────────────┐
 ▼                                        │
[Head | •➔] ➔ [Node 2 | •➔] ➔ [Tail | •➔] ┘
```

### ⚙️ Practical Uses

* **Ring Buffers:** Continuous looping queues without end markers.
* **OS Scheduling:** Round-robin allocation of CPU time to tasks.

### 🧠 Complexity Analysis

* **Access / Search:** O(n)
* **Insertion / Deletion (at Head/Tail with Tail Pointer):** O(1)
* **Space Complexity:** O(n)

### 💻 Python Implementation

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
```
---
🚀 **Happy Coding!** Feel free to clone this repository and practice these methods.


## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
   python3 02_Algorithms/02_Sorting/merge_sort.py
   ```
