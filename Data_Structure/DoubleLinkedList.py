# Adding and Traverse the double linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def printElement(self):
        if self.head is None:
            print("Double linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--> ",end=' ')
                n = n.nref
    
    def add_begin(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nref = self.head
            self.head.pref = newNode
            self.head = newNode


dll1 = DoubleLinkedList()
dll1.add_begin(5)
dll1.add_begin(3)
dll1.add_begin(4)
dll1.printElement()