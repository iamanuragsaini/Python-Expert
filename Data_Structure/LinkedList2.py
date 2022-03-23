# Delete nodes in a Linked List

# class None
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# create a linked List class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # For traversing the data
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--> ",end= '')
                n = n.ref
    
    # Add data in the beginning
    def add_begin(self,data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    # add data in the ending
    def add_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode
    
    # Delete data in the beginning
    def delete_begin(self):
        if self.head is None:
            print("Linked list is already empty!!")
        else:
            self.head = self.head.ref
        
    # Delete data in the ending
    def delete_end(self):
        if self.head is None:
            print("Linked List already empty!!")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            


ll1 = LinkedList()
ll1.add_begin(5)
ll1.add_begin(6)
ll1.add_end(4)
ll1.add_end(3)
ll1.delete_begin()
ll1.delete_end()
ll1.printLinkedList()



