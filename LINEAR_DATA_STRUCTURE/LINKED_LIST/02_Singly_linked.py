# ----CODE1---- #
# Making a Single linked list.

class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

# Print the LL
    def printLL(self):
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")

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
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")
        

obj = SinglyLinkedList()
obj.at_end(10)
obj.at_end(20)
obj.at_end(30)
obj.printLL()
'''output = 10 -> 20 -> 30 -> None'''

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
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")
obj = Singly_LinkedList()
obj.at_beg(10)
obj.at_beg(20)
obj.at_beg(30)
obj.printLL()
'''output = 30 -> 20 -> 10 -> None'''

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

        while(t1 is not None):
            if(t1.info==x):
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
        print(f"Value '{x}' not found in the list.")

    def printll(self):
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")



# ----CODE4---- #
# Deleting a element

def deletell(self, value):
    # 1. Handle empty list
    if self.head is None:
        print("List is Empty")
        return
        
    # 2. Handle deleting the head
    if self.head.info == value:
        self.head = self.head.next
        return
        
    # 3. Handle deleting any subsequent node
    t1 = self.head
    while t1.next is not None:
        if t1.next.info == value:
            t1.next = t1.next.next  # Bypass the target node
            return                  # Node deleted, exit function
        t1 = t1.next                # Advance normally
    print(f"Value '{value}' not found in the list.")


# ----CODE5---- #
# Making a fully functional linked list


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

        while(t1 is not None):
            if(t1.info==x):
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
        print(f"Value '{x}' not found in the list.")
# Insertion at the Beginning
    def  at_beg(self,value):
            temp = node(value)
            temp.next = self.head
            self.head = temp
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
# Delete the Element
    def deletell(self, value):
        if self.head is None:
            print("List is Empty")
            return
        
        if self.head.info == value:
          self.head = self.head.next
          return
        
        t1 = self.head
        while t1.next is not None:
          if t1.next.info == value:
            t1.next = t1.next.next  
            return                 
          t1 = t1.next 
        print(f"Value '{value}' not found in the list.")
# Print the List
    def printll(self):
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")
        
        
a = Singly_LinkedList()
a.at_end(30)
a.at_beg(10)
a.at_mid(20,10)
a.at_mid(40,30)
a.printll()
'''output = 10 -> 20 -> 30 -> 40 -> None'''

a.deletell(30)
a.printll()
'''output = 10 -> 20 -> 40 -> None'''