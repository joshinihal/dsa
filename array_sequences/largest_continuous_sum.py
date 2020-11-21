def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    
    max_sum = current_sum = arr[0]
    #start the range from second element
    for num in arr[1:]:
        current_sum = max(num + current_sum, num)
        max_sum = max(current_sum, max_sum)
    return max_sum
    
    large_cont_sum([-1,2,3,4,-2,4,6,8,4,5,-5])
