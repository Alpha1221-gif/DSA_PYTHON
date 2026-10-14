# Code for a Queue 

class Queue:
    def __init__(self):
        # Initialize an empty list to store queue items
        self.items = []

    def enqueue(self, value):
        # Add an item to the BACK of the queue
        self.items.append(value)

    def dequeue(self):
        # Check if empty using our existing helper method
        if self.isempty():
            return "Queue is Empty"
        # Remove and return the item from the FRONT of the queue
        return self.items.pop(0)

    def peek(self):
        if self.isempty():
            return "Queue is Empty"
        # Look at the FRONT item (FIFO) without removing it
        return self.items[0]
    
    def isempty(self):
        # Returns True if empty, False if it has items
        return len(self.items) == 0

    def length(self):
        return len(self.items)

# --- How to use it ---
q = Queue()
q.enqueue("Alice")
q.enqueue("Bob")

print(q.peek())      # Output: Alice (She is first in line)
print(q.dequeue())   # Output: Alice (Removed from line)
print(q.length())    # Output: 1 (Only Bob is left)


# Code for a Deque

class Deque:
    def __init__(self):
        # Initialize an empty list to store Deque items
        self.items = []

    def insert_at_big(self,value):
        # Add an item to the BEGINNING of the Deque
        self.items.insert(0,value)

    def insert_at_end(self,value):
        # Add an item to the END of the Deque
        self.items.append(value)

    def remove_big(self):
        # Check if empty using our existing helper method
        if self.is_empty():
            return "List is Empty"
        # Remove and return the item from the BEGINNING of the Deque
        return self.items.pop(0)
    
    def remove_end(self):
        # Check if empty using our existing helper method
        if self.is_empty():
            return "List is Empty"
        # Remove and return the item from the END of the Deque
        return self.items.pop()

    def peek_big(self):
        if self.is_empty():
            return "Queue is Empty"
        # Look at the FRONT item (FIFO) without removing it
        return self.items[0]

    def peek_end(self):
        if self.is_empty():
            return "Queue is Empty"
        # Look at the FRONT item (FIFO) without removing it
        return self.items[-1]

    def is_empty(self):
        # Returns True if empty, False if it has items
        return len(self.items) == 0

    def length(self):
        return len(self.items)

# 1. Initialize the Deque
dq = Deque()
print(f"Is deque empty? {dq.is_empty()}")  # True

# 2. Insert items at the end
print("\n--- Inserting items at the end ---")
dq.insert_at_end(20)
dq.insert_at_end(30)
print(f"Current items: {dq.items}")  # [20, 30]

# 3. Insert items at the beginning (front)
print("\n--- Inserting items at the beginning ---")
dq.insert_at_big(10)
dq.insert_at_big(5)
print(f"Current items: {dq.items}")  # [5, 10, 20, 30]
print(f"Deque length: {dq.length()}")  # 4

# 4. Peek at items from both ends
print("\n--- Peeking at items ---")
print(f"Peek Big (Front): {dq.peek_big()}") # 5
print(f"Peek End (Last): {dq.peek_end()}")  # 30

# 5. Remove items from both ends
print("\n--- Removing items ---")
print(f"Removed from front: {dq.remove_big()}")  # Removes 5
print(f"Removed from end: {dq.remove_end()}")    # Removes 30
print(f"Final items in deque: {dq.items}")       # [10, 20]


# Code for a Circular Queue

