# Given the root of a binary search tree and 2 numbers min and max,
# trim the tree such that all the numbers in the new tree are between min and max (inclusive).
# The resulting tree should still be a valid binary search tree.

def trimBST(tree, minVal, maxVal):
    
    if not tree:
        return
    
    tree.leftChild = trimBST(tree.leftChild, minVal, maxVal)
    tree.rightChild = trimBST(tree.rightChild, minVal, maxVal)
    
    if minVal <= tree.value <= maxVal:
        return tree.value
    if tree.value < minVal:
        return tree.rightChild
    if tree.value > maxVal:
        return tree.leftChild
