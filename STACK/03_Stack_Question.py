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


# ----CODE3---- #
# Goal: Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) constant time.

class Minstack:
    def __init__(self):
         # The main stack stores all our actual values
        self.Main_stack = []
        # The min stack tracks the smallest value at each corresponding level
        self.Min_stack = []

    def push(self,val:int) -> None:
        self.Main_stack.append(val)
         # If min_stack is empty, this value is automatically the minimum.
        # Otherwise, compare val with the current minimum at the top of min_stack
        if not self.Min_stack:
            self.Min_stack.append(val)
        else:
            current_min = self.Min_stack[-1] 
            self.Min_stack.append(min(val,current_min))   

    def pop(self)->None:
        if self.Main_stack:
            self.Main_stack.pop()
            self.Min_stack.pop()

    def top(self)->int:
        if self.Main_stack:
            return self.Main_stack[-1]
        return -1  # Default fallback if stack is empty

    def GetMin(self)->int:
        if self.Min_stack:
            return self.Min_stack[-1]
        return -1  # Default fallback if stack is empty
# --- Example Usage ---
# 1. Initialize our special stack object
my_stack = Minstack()

# 2. Push elements
my_stack.push(63)
my_stack.push(98)
my_stack.push(65)
my_stack.push(66)

# 3. Test operations
print("Current Top:", my_stack.top())       # Output = 6
print("Current Minimum:", my_stack.GetMin()) # Output = 6

# 4. Remove the top element (7)
my_stack.pop()

# 5. Check minimum again
print("New Top:", my_stack.top())           # Output = 6
print("New Minimum:", my_stack.GetMin())   #output = 6



# ----CODE4---- #
#Write a function decimal_to_binary(num: int) -> str that uses a stack to convert a positive decimal number into its binary equivalent string

class BinaryConverter:
    def decimal_to_binary(self,num:int) -> str:
        if num == 0:
            return "0"
        stack = []

        while num >0:
         stack.append(num%2)
         num = num // 2

        binary_str = ""
        while stack:
            binary_str += str(stack.pop())
        return binary_str

converter = BinaryConverter()
print(converter.decimal_to_binary(25))    #output = 11001



# ----CODE5---- #
#Given an array, find the next greater element for each element. The next greater element is the first larger element to its right. If none exists, return -1.


class ElementFinder:
    @classmethod
    def next_greater_element(self,arr:list[int]) ->list[int]:
        n = len(arr)       
        result = [-1]*n
        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] < arr[i]:
                prev_index = stack.pop()
                result[prev_index] = arr[i]
            stack.append(i)

        return result
nums = [3,25,25,-4,56]
print(ElementFinder.next_greater_element(nums))
#output = [25, 56, 56, 56, -1]