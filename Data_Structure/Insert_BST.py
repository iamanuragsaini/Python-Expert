# Insert nodes in Binary Search Tree

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
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
            if self.rchild is None:
                self.rchild.insert(key)
            else:
                self.rchild = BST(key)
    
