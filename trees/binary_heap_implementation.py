# min heap implementation
# https://en.wikipedia.org/wiki/Binary_heap

# list has a '0' element at first index(0) i.e. [0,.....]

class BinHeap():
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def perUp(self, i):
        
        while i // 2 > 0:
            
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    
    
#     insert by appending at the end of the list
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
#         since inserting at the end disturbs the heap property,
#         use percUp to push the newly added element upwards to satisy the heap property
        self.percUp(self.currentSize)
        
#         find the min child for an index ,
#        if min child is smaller than the parent percdown the parent
    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
        
    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:
            
            return i * 2
        else:
            
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
#     delete by removing the root since in min heap root is the minimum.
    def delMin():
        rootVal = self.heapList[1]
#         restore the size
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
#     since deleting disturbs the heap size, use percDown to put the min at root
        self.percDown(1)
        return rootVal
        
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
