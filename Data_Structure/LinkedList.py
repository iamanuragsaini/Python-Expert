# To create a linked List

# Create a node class

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class linkedList:
    def __init__(self):
        self.head = None

# Traverse or print our linked List    
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"-->",end=' ')
                n = n.ref
    
# Insert element in the begin
    def add_begin(self,data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

# Insert element in the ending
    def add_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode

# Insert element in the middle

    def add_middle(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        
        if n is None:
            print("Node is not present!!")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode


ll1 = linkedList()


ll1.add_begin(2)
ll1.add_begin(1)
ll1.add_middle(3,2)
ll1.add_end(4)
ll1.add_end(5)

ll1.printLinkedList()
