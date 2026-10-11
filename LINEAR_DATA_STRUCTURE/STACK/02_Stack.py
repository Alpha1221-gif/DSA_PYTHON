# Code for a STACK

class Stack:
    def __init__(self):
        self.items = []
    def push(self,value):
        """Add an item to the top of the stack."""
        self.items.append(value)
    def pop(self):
        """Remove and return the top item."""
        if self.items is None:
            return "Stack is empty"
        else:
            return self.items.pop()
    def peek(self):
        """Look at the top item without removing it."""
        if self.items is None:
            return "Stack is empty"
        else:
            return self.items[-1]
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

s = Stack()

s.push(10)
s.push(20)
s.push(30)
print(s.peek())       # Output: 30
print(s.pop())        # Output: 30
print(s.pop())        # Output: 20
print(s.is_empty())   # Output: False
print(s.size())       # Output: 1