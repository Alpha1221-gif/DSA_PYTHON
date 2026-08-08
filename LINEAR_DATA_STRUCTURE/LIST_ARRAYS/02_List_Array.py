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

# ----CODE3---- #
for i in range(0,11):
    print(val[i],end=" ")
#output = 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0

print('\n') #For space of one line in output
# ----CODE4---- #
for i in val:
    print(i,end=" ")
#output = 1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0


val = array.array('u',['a','b','c','d']) #Here 'u' is used to store string value

# ----CODE3---- #
for i in range(0,len(val)):
    print(val[i],end=" ")
#output = a b c d

print('\n') #For space of one line in output
# ----CODE4---- #
for i in val:
    print(i,end=" ")
#output = a b c d