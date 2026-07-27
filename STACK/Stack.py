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
