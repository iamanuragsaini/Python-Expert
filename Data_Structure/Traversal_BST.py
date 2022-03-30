# Traversal element in the Binary Search Tree

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

# Search element in the tree
    def search(self,key):
        if self.key == key:
            print("Element is present")
            return
        if self.key > key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("Element is not present")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("Element is not present")

# Print in Pre Order manner   
    def print_preorder(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.print_preorder()
        if self.rchild:
            self.rchild.print_preorder()

# Print in In Order manner    
    def print_inorder(self):
        if self.lchild:
            self.lchild.print_inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.print_inorder()

# Print in Post order manner    
    def print_postOrder(self):
        if self.lchild:
            self.lchild.print_postOrder()
        if self.rchild:
            self.rchild.print_postOrder()
        print(self.key, end=' ')


root = BST(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)

print("Pre-Order")
root.print_preorder()
print("\nIn-Order")
root.print_inorder()
print("\nPost-Order")
root.print_postOrder()