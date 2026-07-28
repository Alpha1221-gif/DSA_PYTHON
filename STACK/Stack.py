# ----CODE1---- #
stack = []

#PUSH
stack.append("F")
stack.append("G")
stack.append("H")
stack.append("I")
print("Stack",stack) #output = Stack ['F', 'G', 'H', 'I']

#PEEK
my_top = stack[-1]
print("Top element ",my_top) #output = Top element  I

#POP
pop_element = stack.pop()
print("Pop element ",pop_element) #output = Pop element  I

#Stack after POP
print("Stack after POP ",stack) #output = Stack after POP  ['F', 'G', 'H']

#Is empty
is_empty = not bool(stack)
print("Stack is empty ",is_empty) #output = Stack is empty  False

#LENGTH
print("Length off Stack ",len(stack)) #output = Length off Stack  3


# ----CODE2---- #
class Stack:
    def __init__(self):
        self.stack = []

    def push(self,value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return"Your Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Your stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")

print(my_stack.stack)  #output = ['A', 'B', 'C', 'D']
print(my_stack.pop())  #output = D
print("Stack after pop",my_stack.stack)  #output = Stack after pop ['A', 'B', 'C']
print(my_stack.peek())  #output = C
print(my_stack.is_empty())  #output = False
print(my_stack.size())  #output = 3
