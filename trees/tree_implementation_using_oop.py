# Nodes and References Implementation of a Tree

# defining a class:
# python3 : class BinaryTree()
# older than python 3: class BinaryTree(object)

class BinaryTree():
    
    def __init__(self,rootObj):
#         root value is also called key
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
#     add new as the left child of root, if a node already exists on left, push it down and make it child's child.
    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            
#     add new as the right child of root, if a node already exists on right, push it down and make it child's child.
    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def setRootValue(self,obj):
        self.key = obj
        
    def getRootValue(self):
        return self.key
        
r  = BinaryTree('a')
r.getRootValue()
r.insertLeft('b')
r.getLeftChild().getRootValue()
