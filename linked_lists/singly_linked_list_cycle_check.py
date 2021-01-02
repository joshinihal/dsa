class Node():
    
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        
        
# tortoise-hare algorithm for cycle check
# make two pointers, one will take 1 hops, one will take 2 hops.
# if linked list is cyclic, they will meet. Else, null will come

def cycle_check(node):
    tortoise = node
    rabbit = node
    while rabbit!= None and rabbit.nextnode!= None:
        tortoise = tortoise.nextnode
        rabbit = rabbit.nextnode.nextnode
        if tortoise == rabbit:
            return True
    return False
 
 
a = Node(1)
b = Node(3)
c= Node(5)
a.nextnode = b
b.nextnode = c
c.nextnode =  a
# c.nextnode =  None (for acyclic)


cycle_check(a)
