import ctypes

class DynamicArray(object):
    
    
    def __init__(self):
        
        self.n  = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)
        
            
    def __len__(self):
        
        return self.n
    
    
    def __getitem__(self, k):
        
        if not 0 <= k <= self.n:
            return "Index out of bounds!"
        
        return self.A[k]
    
    
    def append(self, el):
        
        if self.n == self.capacity:
            self._resize(2*self.capacity)
            
        self.A[self.n] = el
        self.n += 1
        
    
    def _resize(self, new_capacity):
        
        B = self.make_array(new_capacity)
        
        for k in range(self.n):
            B[k] = self.A[k]
            
        self.A = B
        self.capacity = new_capacity
        
        
    def make_array(self,capacity):
        
        return (capacity * ctypes.py_object)()
    
    
arr = DynamicArray()

for  i in range(15):
    arr.append(i)

