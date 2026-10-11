# ------------QUESTION(1)------------ #
'''You are attending a party with \(N\) people, labeled from \(0\) to \(N - 1\). 
Among these people, there might be a celebrity. A celebrity is defined as a person 
who fulfills the following two conditions:
1. They are known by everyone else at the party.
2. They do not know anyone else at the party'''

def findCelebrity(mat):
    n = len(mat)
    stack = []

    # Step 1: Push all persons onto the stack
    for i in range(n):
        stack.append(i)

    # Step 2: Eliminate candidates until only one remains
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()

        if mat[a][b] == 1:
            # 'a' knows 'b', so 'a' cannot be a celebrity. 'b' might be.
            stack.append(b)
        else:
            # 'a' does not know 'b', so 'b' cannot be a celebrity. 'a' might be.
            stack.append(a)

    # The last remaining person is our potential celebrity candidate
    candidate = stack.pop()

    # Step 3: Verify the candidate
    for i in range(n):
        if i != candidate:
            # Celebrity must not know anyone, and everyone must know the celebrity
            if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                return -1  # No celebrity found

    return candidate


# Example usage:
# Person 1 is known by 0 and 2, but knows nobody.
mat = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]

print("Celebrity Index:", findCelebrity(mat))  # Output: 1


# ------------QUESTION(2)------------ #
'''Create a data structure twoStacks that represent two stacks. Implementation of 
twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. '''

class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n  # The single array shared by both stacks
        self.top1 = -1         # Pointer for Stack 1 (starts before index 0)
        self.top2 = n          # Pointer for Stack 2 (starts after the last index)

    # --- STACK 1 OPERATIONS ---
    def push1(self, x):
        # Check if there is space between the two pointers
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow! No space left.")

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.arr[self.top1] = None  # Optional: clear the slot
            self.top1 -= 1
            return x
        else:
            print("Stack 1 Underflow! It is empty.")
            return None

    # --- STACK 2 OPERATIONS ---
    def push2(self, x):
        # Check if there is space between the two pointers
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow! No space left.")

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.arr[self.top2] = None  # Optional: clear the slot
            self.top2 += 1
            return x
        else:
            print("Stack 2 Underflow! It is empty.")
            return None

# --- Example Usage ---
ts = TwoStacks(5)  # Create an array of size 5

ts.push1(10)
ts.push1(20)
ts.push2(100)
ts.push2(200)
ts.push1(30)

# Array looks like: [10, 20, 30, 200, 100]

print("Popped from Stack 1:", ts.pop1())  # Outputs 30
print("Popped from Stack 2:", ts.pop2())  # Outputs 200

# ------------QUESTION(3)------------ #
'''Given a string s representing an infix expression ("operand1 operator operand2" ), 
Convert it into its postfix notation ("operand1 operand2 operator").'''

def infixToPostfix(s):
    # Dictionary to define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    stack = []      # Stack to store operators and brackets
    output = []     # List to build the final postfix expression

    for char in s:
        # 1. If character is alphanumeric, it's an operand; add to output
        if char.isalnum():
            output.append(char)
            
        # 2. If it's an opening parenthesis, push to stack
        elif char == '(':
            stack.append(char)
            
        # 3. If it's a closing parenthesis, pop until '(' is found
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove the '(' from the stack
            
        # 4. If it's an operator
        else:
            # Pop operators with higher or equal precedence from the stack
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence.get(char, 0)):
                output.append(stack.pop())
            # Push the current operator onto the stack
            stack.append(char)

    # 5. Pop all remaining operators from the stack
    while stack:
        output.append(stack.pop())

    return "".join(output)

# --- Example Usage ---
expression = "a+b*(c^d-e)^(f+g*h)-i"
print("Infix:  ", expression)
print("Postfix:", infixToPostfix(expression))
# Output: abcd^e-fgh*+^*+i-


'''Prefix to Infix Conversion'''

def isOperator(char):
    return char in {'+', '-', '*', '/', '^'}

def prefixToInfix(prefix_str):
    stack = []
    
    # Scan from right to left (reversing the string)
    for char in reversed(prefix_str):
        
        # 1. If character is an operator
        if isOperator(char):
            # Pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            
            # Combine them: (operand1 + operator + operand2)
            expr = f"({op1}{char}{op2})"
            
            # Push the combined string back to stack
            stack.append(expr)
            
        # 2. If character is an operand, push it to stack
        else:
            stack.append(char)
            
    # The final element left in stack is the infix expression
    return stack.pop()

# --- Example Usage ---
prefix = "*-A/BC-/AKL"
print("Prefix expression: ", prefix)
print("Infix expression:  ", prefixToInfix(prefix))
# Output: ((A-(B/C))*((A/K)-L))
