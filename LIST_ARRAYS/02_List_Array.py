# ----CODE1---- #
# Empty list
a = []
print(a) #output = []

# List with initial values
b = [1, 2, 3, 4, 5]
print(b) #output = [1, 2, 3, 4, 5]

# List with mixed types
c = [1, "hello", 3.14, True]
print(c) #output = [1, 'hello', 3.14, True]

# ----CODE2---- #
d = [9, 12, 7, 4, 11]

# Add element at the last index:
d.append(8)
print(d)  #output = [9, 12, 7, 4, 11, 8]

# Sort list ascending:
d.sort()
print(d)  #output = [4, 7, 8, 9, 11, 12]

# Sort list descending:
d.sort(reverse=True)
print(d)  #output = [12, 11, 9, 8, 7, 4]

# ----CODE3---- #
#Creating Algorithm
my_tuple = (23,45,65,43,17,27,89,87,96,32)
lowest_value = my_tuple[0]
for i in my_tuple:
    if (i<lowest_value):
        lowest_value = i
print("Lowest value is:",lowest_value)    
#output =  [12, 11, 9, 8, 7, 4]