class Node():
    def __init__(self,value):
        self.value = value
        self.next_node = None
        
        
def reverse(head):
    current = head
    previous = None
    nextnode = None
    
#     a(1)->b(2)->c(3)->d(4)->None

    while current:
        nextnode = current.next_node
        current.next_node = previous
        previous = current
        current = nextnode
    return previous


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.next_node = b
b.next_node = c
c.next_node = d

reverse(a)
