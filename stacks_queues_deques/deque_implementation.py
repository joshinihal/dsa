class Deque():
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
#   use array in reverse and consider last index as front
    def addFront(self,item):
        self.items.append(item)
        
#   use array in reverse and consider 0 index as rear
    def addRear(self,item):
        self.items.insert(0,item)
        
#   use array in reverse and consider last index as front        
    def removeFront(self):
        return self.items.pop()
    
#   use array in reverse and consider 0 index as rear
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
d = Deque()
