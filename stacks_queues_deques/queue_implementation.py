class Queue():
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
#     enqueue is the process of adding items to the rear,
#     but use array in reverse and consider 0 index as rear
    def enqueue(self,item):
        self.items.insert(0,item)
        
#     dequeue is the process of removing items from the front,
#     but use array in reverse and consider last index as front
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)

q = Queue()
