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
