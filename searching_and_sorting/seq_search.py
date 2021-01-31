def seq_search(arr,el):
    pos = 0
    found = False
    
    while pos<len(arr) and not found:
        if(arr[pos]==el):
            return True
        else:
            pos+=1
    return False

def ordered_seq_search(arr,el):
    """
    Input arrays must be ordered!
    """
    pos = 0
    found = False
    isGreater = False
    
    while pos<len(arr) and not found and not isGreater:
        if(arr[pos]==el):
            return True
        else:
            if arr[pos]>el:
                isGreater = True
            pos+=1
    return False


seq_search([5,2,1,4,3,6],4)
ordered_seq_search([1,2,3,4,5,6],0)