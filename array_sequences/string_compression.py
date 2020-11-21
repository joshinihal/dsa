# My faster solution
def compress(s):   
    l = len(s)
    if l==0:
        return ''
    compressed_s = s[0]
    count=1
    if l==1:
        return compressed_s+str(count)
    
    for i in range(1,l):
        if s[i] == compressed_s[-1]:
            count+=1
        else:
            compressed_s = compressed_s + str(count)
            count = 1
            compressed_s = compressed_s + s[i]
        if i==l-1:
            compressed_s = compressed_s + str(count)
    return compressed_s

# Jose Portilla's solution
# def compress2(s):
#     """
#     This solution compresses without checking. Known as the RunLength Compression algorithm.
#     """
    
#     # Begin Run as empty string
#     r = ""
#     l = len(s)
    
#     # Check for length 0
#     if l == 0:
#         return ""
    
#     # Check for length 1
#     if l == 1:
#         return s + "1"
    
#     #Intialize Values
#     last = s[0]
#     cnt = 1
#     i = 1
    
#     while i < l:
        
#         # Check to see if it is the same letter
#         if s[i] == s[i - 1]: 
#             # Add a count if same as previous
#             cnt += 1
#         else:
#             # Otherwise store the previous data
#             r = r + s[i - 1] + str(cnt)
#             cnt = 1
            
#         # Add to index count to terminate while loop
#         i += 1
    
#     # Put everything back into run
#     r = r + s[i - 1] + str(cnt)
    
#     return r

compress('aaDDhgDDReeUUxxCfcDDBhjIIUkkL')
