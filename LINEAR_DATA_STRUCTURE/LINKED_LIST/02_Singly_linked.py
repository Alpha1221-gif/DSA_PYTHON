# ----CODE1---- #
# Making a Single linked list.

class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

# Insertion at the end
    def at_end(self,value):
        temp = node(value)
        if(self.head != None): 
            t1 = self.head
            while(t1.next != None):
              t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printLL(self):
        t1 = self.head
        while t1 is not None:  
            print(t1.info)     
            t1 = t1.next  
        

obj = SinglyLinkedList()
obj.at_end(10)
obj.at_end(20)
obj.at_end(30)
obj.printLL()
'''output =10
           20
            30 '''


# ----CODE2---- #

class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class Singly_LinkedList:
    def __init__(self,head=None):
        self.head = head

# Insertion at the beginning
           
    def  at_beg(self,value):
        temp = node(value)
        temp.next = self.head
        self.head = temp

    def printLL(self):
        t1 = self.head
        while t1 is not None:  
            print(t1.info)     
            t1 = t1.next  
obj = Singly_LinkedList()
obj.at_beg(10)
obj.at_beg(20)
obj.at_beg(30)
obj.printLL()
'''output = 30
            20
            10'''


# ----CODE3---- #

class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class Singly_LinkedList:
    def __init__(self,head=None):
        self.head = head

# Insertion at the middle
    
    def at_mid(self,value,x):
        temp = node(value)
        t1 = self.head

        while(t1 != None):
            if(t1.info==x):
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
    def  at_beg(self,value):
            temp = node(value)
            temp.next = self.head
            self.head = temp

    def at_end(self,value):
            temp = node(value)
            if(self.head != None): 
                t1 = self.head
                while(t1.next != None):
                  t1 = t1.next
                t1.next = temp
            else:
                self.head = temp

    def printll(self):
        t1 = self.head
        while(t1 != None):
            print(t1.info)
            t1 = t1.next
        
        
a = Singly_LinkedList()
a.at_end(30)
a.at_beg(10)
a.at_mid(20,10)
a.printll()
'''output =10
           20
        30''' 