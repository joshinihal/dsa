# traverse each root node, then recursively traverse left node, then recursively right  node
def pre_order_traversing(tree):
    if tree != None:
        print(tree.getRootVal())
        pre_order_traversing(tree.getLeftChild())
        pre_order_traversing(tree.getRightChild())
        
# recursively traverse left node, then recursively right, then traverse that root node
def post_order_traversing(tree):
    if tree != None:
        pre_order_traversing(tree.getLeftChild())
        pre_order_traversing(tree.getRightChild())
        print(tree.getRootVal())

# recursively traverse left node, then traverse that root node, then recursively right
def in_order_traversing(tree):
    if tree != None:
        pre_order_traversing(tree.getLeftChild())
        print(tree.getRootVal())        
        pre_order_traversing(tree.getRightChild())
