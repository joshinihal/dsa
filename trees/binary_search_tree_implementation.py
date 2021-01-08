# a binary search tree is a binary tree in which key value smaller than parent key is stored in left subtree 
# and key value larger than parent key in right subtree

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
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not (self.leftChild or self.rightChild)
    
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
            
            
class BinarySearchTree():
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1
        
    def _put(self, key, val, currentNode):
        if key < currentNode.key: 
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                current.leftChild = TreeNode(key, val, parent = currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                current.rightChild = TreeNode(key, val, parent = currentNode) 
    
    def __setitem__(self, key, val):
        self.put(key, val)
        
    def get(self, key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False
        
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1 
        else:
            raise KeyError('Error, key not in tree')
            
    def __delitem__(self, key):
        self.delete(key)
