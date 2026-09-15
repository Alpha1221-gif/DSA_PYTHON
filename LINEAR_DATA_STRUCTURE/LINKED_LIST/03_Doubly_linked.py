class node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self,head=None):
        self.head = head 

# Print the linked list
def printll(self):
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")


# Insertion at the END
def is_end(self,value):
    temp = node(value)
    if(self.head==None):
        self.head = temp
        return
    else:
     t1 = self.head
     while(t1.next!=None):
          t1 = t1.next
     t1.next = temp
     temp.prev = t1

# Insertion at Beginning
def is_big(self,value):
    temp = node(value)
    if(self.head==None):
        self.head = temp
        return
    temp.next = self.head
    self.head.prev = temp
    self.head = temp


# Insertion at Middle
def is_mid(self,value,x):
    if self.head is None:
        print("List is empty.")
        return

    t1 = self.head
    while t1 is not None and t1.value!=x:
        t1 = t1.next

    if t1 is None:
        print(f"Node with value {x} is not found.")
        return

    temp = node(value)
    temp.next = t1.next
    if t1.next is not None:
        t1.next.prev = temp

    t1.next = temp
    temp.prev = t1


# Delete the Linked List
def deletell(self,value):
    if self.head is None:
        print("List is empty")
        return
    
    if self.head.info == value:
        self.head == self.head.next
        if self.head is not None:
            self.head.prev = None
        return

    t1 = self.head
    while t1 is not None and t1.info!=value:
        t1 = t1.next

    if t1 is not None:
        print(f"Value {value} is not found")
        return

    t1.prev.next = t1.next
    if t1.next is not None:
        t1.next.prev = t1.prev


# Full code for Double linked list
class node:
    def __init__(self,info=None):
        self.info = info
        self.next = None
        self.prev = None
class doublelinkedlist:
    def __init__(self,head=None):
        self.head = head
    def is_big(self,value):
        temp = node(value)
        if self.head is None:
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    def is_mid(self,value,x):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head 
        while t1 is not None and t1.info!=x:
            t1 = t1.next
        if t1 is None:
            print(f"Node with these value {x} is not found")
            return
        temp = node(value)
        temp.next = t1.next
        if t1.next!=None:
            t1.next.prev = temp
        t1.next = temp
        temp.prev = t1
    def is_end(self,value):
        temp = node(value)
        if self.head is None:
            self.head = temp
            return
        else:
            t1 = self.head
            while t1.next!=None:
                t1 = t1.next
            t1.next = temp
            temp.prev = t1
    def deletell(self,value):
        if self.head is None:
            print("List is empty")
            return 
        if self.head.info == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        t1 = self.head
        while t1 is not None and t1.info!=value:
            t1 = t1.next
        if t1 is None:
            print(f"Node with these value {value} is not found")
            return
        t1.prev.next = t1.next
        if t1.next is not None:
            t1.next.prev = t1.prev
    def printll(self):
        if self.head is None:
            print("List is empty")
            return
        
        t1 = self.head
        while t1 is not None:  
            print(t1.info,end=" -> ")     
            t1 = t1.next  
        print("None")
a = doublelinkedlist()
a.is_big(10)
a.is_mid(20,10)
a.is_end(30)
a.printll()
"""Output = 10 -> 20 -> 30 -> None """