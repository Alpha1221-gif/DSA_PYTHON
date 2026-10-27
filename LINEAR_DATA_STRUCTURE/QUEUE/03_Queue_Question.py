#  ---- PROBLEM 1 ----  #
# Implement a stack using queue(s). Only queue operations are allowed to perform stack operations.

from collections import deque

class My_stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def is_empty(self):
        return len(self.q1) == 0
    
    def push(self,value):
        self.q2 = deque(self.q1)
        self.q1.clear()
        self.q1.append(value)
        self.q1.extend(self.q2)

    def pop(self):
        if self.is_empty():
            return None
        return self.q1.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.q1[0]

    def display(self):
        """Helper to view current stack elements (Top to Bottom)."""
        print("Stack (Top -> Bottom):", list(self.q1))
s = My_stack()

s.push(10)
s.push(20)
s.push(30)
s.display()  # Stack (Top -> Bottom): [30, 20, 10]

print("Peek:", s.peek())  # Peek: 30
print("Popped:", s.pop())  # Popped: 30
s.display()  # Stack (Top -> Bottom): [20, 10]

print("Popped:", s.pop())  # Popped: 20
print("Popped:", s.pop())  # Popped: 10
print("Popped:", s.pop())  # Stack is empty -> None

#  ---- PROBLEM 2 ----  #

# Implement a queue using stacks. We are allowed to use only stack data structure.

class My_queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def is_empty(self):
        return len(self.s1) == 0

    def push(self,value):
        self.s2 = self.s1.copy()
        self.s1.clear()
        self.s1.append(value)
        self.s1.extend(self.s2)

    def pop(self):
        if self.is_empty():
            return None
        return self.s1.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.s1[-1]
    def display(self):
        print("Queue (Front -> Rear):", list(reversed(self.s1)))

q = My_queue()

q.push(10)
q.push(20)
q.push(30)
q.display()  # Queue (Front -> Rear): [10, 20, 30]

print("Peek:", q.peek())  # Peek: 10
print("Popped:", q.pop())  # Popped: 10

q.display()  # Queue (Front -> Rear): [20, 30]

q.push(40)
q.display()  # Queue (Front -> Rear): [20, 30, 40]

print("Popped:", q.pop())  # Popped: 20
print("Popped:", q.pop())  # Popped: 30
print("Popped:", q.pop())  # Popped: 40
print("Popped:", q.pop())  # Queue is empty -> None


#  ---- PROBLEM 3 ----  #

# Given a queue q[], reverse the queue so that the front element becomes the rear and the rear element becomes the front, while preserving the order of the remaining elements accordingly.

from collections import deque

q = deque([1,2,3,4,5])

print("Original Queue:",list(q)) # Original Queue: [1, 2, 3, 4, 5]
q.reverse()

print("Reversed Queue:",list(q)) # Reversed Queue: [5, 4, 3, 2, 1]

#  ---- PROBLEM 4 ----  #
# Given two integers n and k. Implement k queues using a single array of size n. Multiple queue must share the same array space while supporting the following operations:

class KQueues:
    def __init__(self, k: int, n: int):
        """
        k: number of queues
        n: total capacity of the shared array
        """
        self.k = k
        self.n = n

        # Storage array
        self.arr = [None] * n

        # Queue tracking
        self.front = [-1] * k
        self.rear = [-1] * k

        # Link array: initially links all slots 0 -> 1 -> 2 -> ... -> n-1 -> -1
        self.next_idx = list(range(1, n)) + [-1]

        # Head of the available free slots list
        self.free_head = 0

    def is_full(self) -> bool:
        """Returns True if all n slots are occupied."""
        return self.free_head == -1

    def is_empty(self, qn: int) -> bool:
        """Returns True if queue `qn` (0-indexed) has no elements."""
        return self.front[qn] == -1

    def enqueue(self, item, qn: int) -> bool:
        """Adds `item` to queue `qn` (0-indexed)."""
        if self.is_full():
            print(f"Overflow: Cannot enqueue {item} into queue {qn}. Array is full.")
            return False

        # 1. Grab the next available slot from the free list
        insert_idx = self.free_head
        self.free_head = self.next_idx[insert_idx]

        # 2. Put the data into the allocated slot
        self.arr[insert_idx] = item
        self.next_idx[insert_idx] = -1  # End of this queue's chain

        # 3. Link into queue `qn`
        if self.is_empty(qn):
            self.front[qn] = insert_idx
        else:
            self.next_idx[self.rear[qn]] = insert_idx

        self.rear[qn] = insert_idx
        return True

    def dequeue(self, qn: int):
        """Removes and returns the front item from queue `qn` (0-indexed)."""
        if self.is_empty(qn):
            print(f"Underflow: Queue {qn} is empty.")
            return None

        # 1. Locate the front item
        remove_idx = self.front[qn]
        item = self.arr[remove_idx]

        # 2. Advance the front pointer to the next element
        self.front[qn] = self.next_idx[remove_idx]

        # If the queue is now empty, reset rear pointer as well
        if self.front[qn] == -1:
            self.rear[qn] = -1

        # 3. Return the freed slot back to the free list
        self.next_idx[remove_idx] = self.free_head
        self.free_head = remove_idx

        return item

# Create 3 queues sharing an array of size 10
kq = KQueues(k=3, n=10)

# Enqueue items to different queues
kq.enqueue(15, qn=0)
kq.enqueue(45, qn=1)
kq.enqueue(20, qn=0)
kq.enqueue(30, qn=0)
kq.enqueue(50, qn=2)

print("Dequeued from Queue 0:", kq.dequeue(qn=0))  # Output: 15
print("Dequeued from Queue 1:", kq.dequeue(qn=1))  # Output: 45
print("Dequeued from Queue 0:", kq.dequeue(qn=0))  # Output: 20
print("Dequeued from Queue 2:", kq.dequeue(qn=2))  # Output: 50
print("Dequeued from Queue 0:", kq.dequeue(qn=0))  # Output: 30

# Try to dequeue from an empty queue
print("Dequeued from Queue 0:", kq.dequeue(qn=0))  # Underflow: returns None