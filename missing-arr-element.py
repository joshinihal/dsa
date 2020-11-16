#-----------------------------------------

# Linear time in constant space cmooplexity

# Another soln is to use XOR (if numbers are same, result is zero. Else, result is big - small)

# def finder(arr1,arr2):
#     result = 0
    
#     for num in arr1+arr2:
#         result ^= num # ^= is for XOR
#     return result


#------------------------------------------


# Linear solution O(N)

def finder(arr1, arr2):
    
    d = {}
    
    for num in arr2:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
            
    for num in arr1:
        if num in d:        
            if d[num] == 0:
                return num
            else:
                d[num] -= 1
        else:
            return num
        
#--------------------------------------

# O(NlogN) soln

# def finder(arr1,arr2):
#     arr1.sort()
#     arr2.sort()
    
#     for num1,num2 in zip(arr1,arr2):
#         if num1 != num2:
#             return num1
#     return arr1[-1]


#----------------------------------------



# One soln can be to find the difference of
# addition of all elements of first arr and addition of all elements of second arr

# (sum of all elements of first) - (sum of all elements of second)
# BUT for larger numbers, this can cause overflow or for large decimals, loss of decimals. Therefore, not effecient.

#-----------------------------------------




