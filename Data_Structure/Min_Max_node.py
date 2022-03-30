# Min and Max node in the Binary Search Tree

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

# Inset element in the tree   
    def insert(self,key):
        if self.key is None:
            self.key = key
            return
        if self.key == key:
            return
        if self.key > key:
            if self.lchild:
                self.lchild.insert(key)
            else:
                self.lchild = BST(key)
        else:
            if self.rchild:
                self.rchild.insert(key)
            else:
                self.rchild = BST(key)

# Find min node in the tree
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Min node is : ", current.key)

# Find max node in the tree
    def max_node(self):
        while self.rchild:
            self = self.rchild
        print("Max node is : ", self.key)
            
root = BST(10)
list1 = [6,3,1,98,7]
for i in list1:
    root.insert(i)
root.min_node()
root.max_node()

