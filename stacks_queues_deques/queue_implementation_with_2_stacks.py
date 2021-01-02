class Queue2Stacks():
    
    def __init__(self):
        
        # Two Stacks
        self.instack = []
        self.outstack = []
     
     
    # Since stack only allows adding and removing from one end,
    # two stacks can be chained to implement a queue. 
    # The first stack adds an element from one end, 
    # the second removes from other
    def enqueue(self,element):
        
        self.instack.append(element)
    
    def dequeue(self):
        
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        
