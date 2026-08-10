import array

val = array.array('i',[1,2,3,4,5,6,7,8,9,10]) #Here 'i' is used to store integer value

# ----CODE1---- #
for i in range(0,10):
    print(val[i],end=" ")
#output = 1 2 3 4 5 6 7 8 9 10 

print('\n') #For space of one line in output
# ----CODE2---- #
for i in val:
    print(i,end=" ")
#output = 1 2 3 4 5 6 7 8 9 10


val = array.array('d',[1,2,3,4,5,6,7,8,9,10,11.0]) #Here 'd' is used to store float value
print('\n')
# ----CODE3---- #
for i in range(0,11):
    print(val[i],end=" ")
#output = 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0

print('\n') 
# ----CODE4---- #
for i in val:
    print(i,end=" ")
#output = 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0


val = array.array('w',['a','b','c','d']) #Here 'u' is used to store string value
print('\n')
# ----CODE5---- #
for i in range(0,len(val)):
    print(val[i],end=" ")
#output = a b c d

print('\n') 
# ----CODE6---- #
for i in val:
    print(i,end=" ")
#output = a b c d


print('\n')
# ----CODE7---- #
from array import *
val1 = array('i',[1,2,3,4,5,6])
print(val1.typecode) #output = i
print(type(val1)) #output = <class 'array.array'>


print('\n')
# ----CODE8---- #
from array import *
val2 = array('i',[1,2,3,4,5,6])
val2.reverse() #For reverse a array
for i in val2:
    print(i,end=" ")  #output = 6 5 4 3 2 1


print('\n')
# ----CODE9---- #
from array import *
val3 = array('i',[1,2,3,4,5,6])
val3.insert(0,0) #For insert a value in array with your own choice index
for i in val3:
    print(i,end=" ")  #output = 0 1 2 3 4 5 6


print('\n')
# ----CODE10---- #
from array import *
val4 = array('i',[1,2,3,4,5,6])
val4.append(7) #For insert a value in array at last index
for i in val4:
    print(i,end=" ")  #output =  1 2 3 4 5 6 7


print('\n')
# ----CODE11---- #
from array import *
val5 = array('i',[1,2,3,8,5,6])
val5[3] = 4 #For replace a value in array at 
for i in val5:
    print(i,end=" ")  #output =  1 2 3 4 5 6 


print('\n')
# ----CODE12---- #
from array import *
val6 = array('i',[1,2,3,4,5,6])
copyarray = array(val6.typecode,(x for x in val6)) #For copy the value in copyarray from val6
for i in range(0,len(val6)):
    print(copyarray[i],end = " ")  #output =  1 2 3 4 5 6 


print('\n')
# ----CODE13---- #
from array import *
val7 = array('i',[1,2,3,4,5,6])
copyarray = array(val6.typecode,(x for x in val6)) 
copyarray.pop(4) #Used for remove a element by using a index
for i in range(0,len(copyarray)):
    print(copyarray[i],end = " ")  #output =  1 2 3 4 6


print('\n')
# ----CODE14---- #
from array import *
val8 = array('i',[1,2,3,4,5,6])
copyarray = array(val6.typecode,(x for x in val6)) 
copyarray.remove(2) #Used for remove a particular element 
for i in range(0,len(copyarray)):
    print(copyarray[i],end = " ")  #output =  1 3 4 5 6


print('\n')
# ----CODE15---- #
from array import *
val9 = array('i',[1,2,3,4,5,6])
a = val9[3:6] #Slicing
for i in a:
    print(i,end= " ")  #output = 4 5 6


print('\n')
# ----CODE16---- #
from array import *
val9 = array('i',[1,2,3,4,5,6])
a = val9[::-1] # Reverse a Array
for i in a:
    print(i,end= " ")  #output = 6 5 4 3 2 1


print('\n')
# ----CODE17---- #
from array import *
val10 = array('i',[])
n = int(input("Enter the total no:")) # Print and store the user input values 
for i in range(0,n):
    val10.append(int(input("Enter the no:")))

for x in val10:
    print(x,end= " ")
'''Enter the total no:5
Enter the no:5
Enter the no:4
Enter the no:3
Enter the no:2
Enter the no:1
5 4 3 2 1 '''