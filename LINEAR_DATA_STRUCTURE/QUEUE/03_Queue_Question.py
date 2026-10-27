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