#  FOR A SINGLY LINKED LIST

class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
class circularlinkedlist:
    def __init__(self,head=None):
        self.head = head
    def at_beg(self,value):
        temp = node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head
            return

        t1 = self.head
        while t1.next!=self.head:
            t1 = t1.next
        temp.next = self.head
        t1.next = temp
        self.head = temp
    def at_mid(self,value,x):
        if self.head is None:
            print("List is Empty")
            return

        temp = node(value)
        t1 = self.head
        while True:
            if t1.info==x:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next
            if t1 == self.head:
                break
        print(f"Node {x} Not Found")
    def at_end(self,value):
        temp = node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head
            return
        t1 = self.head
        while t1.next!=self.head:
            t1 = t1.next
        t1.next = temp
        temp.next = self.head
    def deletell(self,value):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.info==value:
            if self.head.next==self.head:
                self.head = None
                return
            t1 = self.head
            while t1.next!=self.head:
               t1 = t1.next
            t1.next = self.head.next
            self.head = self.head.next
            return
        t1 = self.head
        while t1.next!=self.head:
            if t1.next.info==value:
                t1.next = t1.next.next
                return
            t1 = t1.next
        print(f"Node {value} not found")
    def printll(self):
        if self.head is None:
            print("List is Empty")
            return

        t1 = self.head
        while True:
            print(t1.info,end=" -> ")
            t1 = t1.next
            if t1==self.head:
                break
        print("(head)")

cll = circularlinkedlist()

# Insertions
cll.at_end(30)       # [30] -> points to 30
cll.at_beg(10)       # 10 -> 30 -> (head)
cll.at_mid(20, 10)   # Insert 20 after 10: 10 -> 20 -> 30 -> (head)
cll.at_mid(40, 30)   # Insert 40 after 30: 10 -> 20 -> 30 -> 40 -> (head)

cll.printll()
# Output: 10 -> 20 -> 30 -> 40 -> (back to head)

# Deletions
cll.deletell(30)     # Delete from middle
cll.printll()
# Output: 10 -> 20 -> 40 -> (back to head)

cll.deletell(10)     # Delete the head
cll.printll()
# Output: 20 -> 40 -> (back to head)
            
        
# FOR A DOUBLY LINKED LIST

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning
    def is_big(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp
            temp.prev = temp
            return

        last = self.head.prev

        temp.next = self.head
        temp.prev = last
        last.next = temp
        self.head.prev = temp

        self.head = temp

    # Insertion after value 'x'
    def is_mid(self, value, x):
        if self.head is None:
            print("List is empty")
            return

        t1 = self.head
        while True:
            if t1.info == x:
                temp = Node(value)
                temp.next = t1.next
                temp.prev = t1
                t1.next.prev = temp
                t1.next = temp
                return

            t1 = t1.next
            if t1 == self.head:
                break

        print(f"Node with value {x} is not found")

    # Insertion at the end
    def is_end(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = temp
            temp.prev = temp
            return

        last = self.head.prev

        last.next = temp
        temp.prev = last
        temp.next = self.head
        self.head.prev = temp

    # Delete a node by value
    def deletell(self, value):
        if self.head is None:
            print("List is empty")
            return

        t1 = self.head
        while True:
            if t1.info == value:
                # Case 1: Only one node in the list
                if t1.next == t1:
                    self.head = None
                    return

                # Case 2: Deleting the head node
                if t1 == self.head:
                    self.head = t1.next

                # Rewire neighbors to bypass t1
                t1.prev.next = t1.next
                t1.next.prev = t1.prev
                return

            t1 = t1.next
            if t1 == self.head:
                break

        print(f"Node with value {value} is not found")

    # Forward traversal
    def printll(self):
        if self.head is None:
            print("List is empty")
            return

        t1 = self.head
        while True:
            print(t1.info, end=" <-> ")
            t1 = t1.next
            if t1 == self.head:
                break
        print("(head)")


# Driver code with values
a = CircularDoublyLinkedList()
a.is_big(10)
a.is_mid(20, 10)
a.is_end(30)
a.printll()
# Output: 10 <-> 20 <-> 30 <-> (head)

a.deletell(20)
a.printll()
# Output: 10 <-> 30 <-> (head)




        