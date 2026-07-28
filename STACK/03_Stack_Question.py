# ----CODE1---- #
#Write a function that uses a stack to reverse any text input (e.g., "hello" becomes "olleh")

class stack:
    def __init__(self):
        self.items = []

    def push(self,items):
        self.items.append(items)

    def pop(self):
        if self. is_empty():
            return "stack is empty"
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reversed_string(text):
    my_stack = stack()

    for i in text:
        my_stack.push(i)

    reversed_string = ""

    while not my_stack.is_empty():
        reversed_string += my_stack.pop()
    return reversed_string
word = "hello"
result = reversed_string(word)

print("original text:",word)  #output = original text: hello
print("reversed text:",result)  #output = reversed text: olleh

# ----CODE2---- #
#Write a function that checks if brackets in a string are closed correctly.

class Stack:
    def __init__(self):
      self.items = []

    def push(self,value):
        self.items.append(value)

    def pop(self):
        if self. is_Empty():
            return "Stack is empty"
        return self.items.pop()
    
    def is_Empty(self):
        return len(self.items) == 0
    
def bracket_checker_function(text):
    my_stack = Stack()

    matching_pairs = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
    }

    for i in text:
        if i in [ "{","[","("]:
            my_stack.push(i)
        elif i in [")","}","]"]:
            if my_stack.is_Empty():
                return False
            
            
            top_item = my_stack.pop()
            
            
            if top_item != matching_pairs[i]:
                return False  # Mismatch found! (e.g., ( ] )
                
    
    return my_stack.is_Empty()



print(bracket_checker_function("()"))      # True (Perfect match)
print(bracket_checker_function("([{}])"))  # True (Perfect nested match)
print(bracket_checker_function("(]"))      # False (Wrong closing bracket)
print(bracket_checker_function("(()"))     # False (An opening bracket was left unclosed)
print(bracket_checker_function(")"))      # False (Closing bracket with nothing to open it)