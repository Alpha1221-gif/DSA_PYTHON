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
        self.prev = None
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


# (3) = Given a singly linked list and a key, the task is to count the number of occurrences of the given key in the linked list.
     
class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next
class singlylinkedlist:
    def __init__(self,head=None):
        self.head = head
    def count(self,k):
        if self.head is None:
            print("List is Empty")
            return
        t1 = self.head
        count = 0
        while t1 is not None:
            if t1.info==k:
                count += 1
            t1 = t1.next
        return count       


# (4) = Given the head of a circular linked list, print the data of the nodes in the linked list starting from the head node, traversing the list exactly once.

# For Singly linked list and Doubly linked list
class linkedlist:
    def printll(self):
        if self.head is None:
            print("List is empty!")
            return
        t1 = self.head
        while True:
            print(t1.info,end=" ")
            t1 = t1.next
            if t1 == self.head:
                break
        print("(Head)")


# (5) = Given the head of a singly linked list, the task is to find if given linked list is circular or not.

class linkedlist:
    def check(self):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head.next

        # Traverse until we hit None or come back to head
        while t1 is not None and t1!=self.head:
            t1 = t1.next

        if t1 == self.head:
            print("Cll")
        if t1 == None:
            print("SLL")

# Approach 2: Floyd's Cycle Detection (Tortoise and Hare)

class linkedlist:
    def check(self):
        if self.head is None:
            return "List is empty"

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return "CLL"  # Cycle detected

        return "SLL"


# (6) = The task is to find the length of the linked list, where length is defined as the number of nodes in the linked list.

class node:
    def __init__(self,info):
        self.info = info
        self.next = None
        self.prev = None
class doublylinkedlist:
    def __init__(self,head=None):
        self.head = head
    def count_length(self):
        if self.head is None:
            print("List is empty")
            return
        t1 = self.head
        count = 0
        while t1 is not None:
            count+=1
            t1 = t1.next
        return count


# (7) = Reverse a Linked List

# For a Singly Linked List
class node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = None
class singlylinkedlist:
    def __init__(self,head=None):
        self.head = head
    def reverse(self):
        if self.head is None:
            print("List is empty")
            return
        prev = None
        t1 = self.head

        while t1 is not None:
            next_node = t1.next  # 1. Save next node
            t1.next = prev       # 2. Reverse current node's pointer
            prev = t1            # 3. Move prev forward
            t1 = next_node       # 4. Move current forward

        self.head = prev  # Reset head to the new front

# For a Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        # Empty list or single node requires no changes
        if self.head is None or self.head.next is None:
            return

        t1 = self.head
        temp = None

        while t1 is not None:
            # Swap next and prev pointers
            temp = t1.prev
            t1.prev = t1.next
            t1.next = temp

            # Move to the next node (which is now stored in t1.prev)
            t1 = t1.prev

        # After the loop, temp points to the prev of the last processed node,
        # so temp.prev is the new head node.
        if temp is not None:
            self.head = temp.prev


            

