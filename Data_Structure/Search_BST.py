# Search element in the Binary Search Tree 

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
  
# Insert element in the tree
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

# Search element in the tree
    def search(self,key):
        if self.key == key:
            print("Node is present")
            return
        if key < self.key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("Node is not present")





b1 = BST(10)
b1.insert(5)
b1.insert(4)
b1.insert(6)
b1.search(4)
