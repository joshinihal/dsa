# Given an integer array, output all the unique pairs that sum up to a specific value k.

# O(n^2) solution
# def pairsum(arr, number):
    
#     pairs = []
    
#     for i in arr:
#         for j in arr:
#             if i+j == number and ((i,j) not in pairs) and ((j,i) not in pairs) and arr.index(i) != arr.index(j):
#                 pairs.append((i,j))
    
#     return pairs

# ------------------------------------

# O(n) solution

def pairsum(arr,k):
    
    if len(arr)<2:
        return
    
    # use sets to track
    
    seen = set()
    output = set()
    
    for number in arr:
        
        target = k - number
        
        if target not in seen:
            seen.add(number)
            
        else:
            output.add( ( min(target,number) , max(target,number) ) )
        
#     return len(output)
    print ('\n'.join(map(str,list(output))))
    
    
pairsum([1,3,2,2,4,5,6,7,8,8,9,0],10)
