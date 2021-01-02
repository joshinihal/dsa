class Node():
    def __init__(self,value):
        self.value = value
        self.next_node = None

def nth_to_last_node(n,head):
    start = head
    end = head
    
    for i in range(n):
        if not start.next_node:
            raise LookupError('Error: n is larger than the linked list')
        end = end.next_node
    
    while end.next_node:
        start = start.next_node 
        end = end.next_node 
        
    return start
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e

# This would return the node d with a value of 4, because its the 2nd to last node (2nd last or penultimate ).
# (3,a) would return 3rd last, (4,a) would 4th last.
nth_to_last_node(2, a)
