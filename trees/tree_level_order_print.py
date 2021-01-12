import collections 

class Node():
    def __init__(self, val= None):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        
def level(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1,0
#   same as currentCount = 1 nextCount = 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount = currentCount - 1
        print(currentNode.val,end = '')
        if currentNode.leftChild:
            nodes.append(currentNode.leftChild)
            nextCount = nextCount + 1
        if currentNode.rightChild:
            nodes.append(currentNode.rightChild)
            nextCount = nextCount + 1
        if currentCount == 0:
#             finished printing current level            
            print('\n')
            currentCount, nextCount = nextCount, currentCount

my_tree = Node(1)
my_tree.leftChild = Node(2)
my_tree.rightChild = Node(3)
level(my_tree)
