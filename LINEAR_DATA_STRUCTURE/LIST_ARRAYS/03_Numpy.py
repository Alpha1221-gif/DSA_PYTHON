# ----CODE1---- #
from numpy import * 

val = array([1,2,3])
for i in val:
    print(i)
'''output = 1
            2
            3'''


print('\n')
# ----CODE2---- #
from numpy import * 

val1 = array([1,2,3],float)
for i in val1:
    print(i,end=" ")
#output = 1.0 2.0 3.0 


print('\n')
# ----CODE3---- #
from numpy import * 

val2 = linspace(10,40,5)  #  Generates 5 equally spaced numbers from 10 to 40
for x in val2:
    print(x,end=" ")
#output = 10.0 17.5 25.0 32.5 40.0


print('\n')
# ----CODE4--- #
from numpy import * 

val3 = arange(10,40,5)  #  Generates numbers from 10 up to (but excluding) 40, stepping by 5
for x in val3:
    print(x,end=" ")
#output = 10 15 20 25 30 35


print('\n')
# ----CODE5--- #
from numpy import * 

val4= logspace(1,4,4) # Generates 4 numbers from 10^1 (10) to 10^4 (10000)
for x in val4:
    print(x,end=" ")
#output = 10.0 100.0 1000.0 10000.0 


print('\n')
# ----CODE6--- #
from numpy import * 

val5= zeros(5) # Creates a 1D array of five zeros
for a in val5:
    print(a,end=" ")
#output = 0.0 0.0 0.0 0.0 0.0


print('\n')
# ----CODE7--- #
from numpy import * 

val6= ones(5) # Creates a 1D array of five ones
for b in val6:
    print(b,end=" ")
#output = 1.0 1.0 1.0 1.0 1.0


print('\n')
# ----CODE8--- #
from numpy import * 

val7= full(5,3) #  creates a new array of a specified shape filled entirely with a custom value.
for c in val7:
    print(c,end=" ")
#output = 3 3 3 3 3


print('\n')
# ----CODE9--- #
# Zero Dimensional array

zero = array(10)
print(zero) #output = 10

# One Dimensional array

one = array([1,2,3,4,5])
print(one) #output = [1 2 3 4 5]

# Two Dimensional array = Collection of One Dimensional array

two = array([[1,2,3],[4,5,6],[7,8,9]])
print(two) 
'''[[1 2 3]
 [4 5 6]
 [7 8 9]]'''

# Three Dimensional array = Collection of Two Dimensional array

three = array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(three) 
'''[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]'''