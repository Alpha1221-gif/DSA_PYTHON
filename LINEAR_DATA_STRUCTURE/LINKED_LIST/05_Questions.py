# (1) = Given a singly linked list head , The task is to remove every kth node from the linked list

class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
class singlylinkedlist:
    def __init__(self,head=None):
        self.head = head

    def remove_kth(self,k):
        # Base case 1: If the list is empty, do nothing
        if self.head is None:
            print("List is empty")
            return
        # Base case 2: If k is 1, delete all nodes (list becomes empty)
        if k == 1:
            self.head = None
            return
        
        t1 = self.head
        prev = None
        count = 0

        while t1 is not None:
            count += 1
         # If we reached the k-th node, delete it
            if count == k:
                prev.next = t1.next
                count = 0
            # Only move prev forward if we didn't delete the node
            else:
                prev = t1

            t1 = t1.next

# (2) = Given the head of singly linked list, find middle node of the linked list.

# For Singlylinked list
class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
class singlylinkedlist:
    def __init__(self,head=None):
        self.head = head
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return
        slow = self.head
        fast = self.head

         # Fast runner moves 2 steps, Slow runner moves 1 step
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

         # When fast reaches the end, slow is exactly at the middle node
        return slow

# For DoublyLinked list
class node:
    def __init__(self,info=None):
        self.info = info
        self.next = None
        self.head = None
class doublylinkedlist:
    def __init__(self,head=None):
        self.head = head
    def find_middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
        

            


