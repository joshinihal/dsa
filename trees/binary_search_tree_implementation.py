# a binary search tree is a binary tree in which node value smaller than parent is stored in left subtree 
# and node value larger than parent in right subtree

class TreeNode():
    
    def __init__(self, key, value, left=None, right=None, parent=None ):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        
    def hasLeftChild(self):
        return self.leftChild
    
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.rightChild == self
