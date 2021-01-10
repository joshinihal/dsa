# pythonic solution

# tree_vals = []

# def inorder(tree):
#     tree.inorder(tree.getLeftChild())
#     tree_vals.append(tree.getRootval())
#     tree.inorder(tree.getRightChild())

# def sort_check(tree_vals):
#     return tree_vals == sorted(tree_vals)

# inorder(tree)
# sort_check(tree_vals)

# ---------------------------------------------

# general solution

class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.rightChild = None
        self.leftChild = None
    

def tree_max(node):
#     check for a base case, if the node doesn't exist,
#     return lowest value possible so that it doesn't win
#     when comparing using max function
    if not node:
        return float('-inf')
    max_left = tree_max(node.leftChild)
    max_right = tree_max(node.rightChild)
    return max(max_left, node.key, max_right)
                        
def tree_min(node):
#     check for a base case, if the node doesn't exist,
#     return highest value possible so that it doesn't win
#     when comparing using min function
    if not node:
        return float('inf')
    min_left = tree_min(node.leftChild)
    min_right = tree_min(node.rightChild)
    return min(min_left, node.key, min_right)

def verify(node):
    if not node:
        return True
    if (tree_max(node.leftChild)<= node.key <= tree_min(node.rightChild)
        and verify(node.leftChild) and verify(node.rightChild)):
        return True
    else: 
        return False


root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print(verify(root)) # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root)) # prints False, since 15 is to the left of 10
