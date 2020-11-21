# Manual implementation
def reverse(str):
    start_exists = False
    arr = []
    rev = ''
    len_of_str = len(str)
    for i in range(len(str)):
        if str[i] != ' ':
            if start_exists == False:
                start_index = i
            start_exists = True
        if str[i] == ' ' and start_exists == True:
            end_index = i
            arr.append(str[start_index:end_index])
            start_exists = False
        if i==len_of_str-1 and start_exists == True:
            end_index = len_of_str
            arr.append(str[start_index:end_index])
            start_exists = False
            
    for i in range(len(arr)-1,-1,-1):
        rev = rev + arr[i] + ('' if i == 0 else ' ')
    return rev

# Using reversed function implementation
# def rev_word3(s):
#     words = []
#     len_of_str = len(s)
#     spaces = [ ' ']
#     i = 0
#     while i < len_of_str:
#         if s[i] not in spaces:
#             start_index = i
#             while i < len_of_str and s[i] not in spaces:
#                 i += 1
#             words.append(s[start_index:i])
#         i += 1
        
#     return ' '.join.reversed(words)

# Using reversed function and split implementation
# def rev_word1(s):
#     return " ".join(reversed(s.split()))

reverse(' Hi     how are      you doing     today')
