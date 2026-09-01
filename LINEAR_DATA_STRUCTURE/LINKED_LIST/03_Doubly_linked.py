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
    t1 = self.head
    while t1!=None:
        print(t1.value)
        t1 = t1.next


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
