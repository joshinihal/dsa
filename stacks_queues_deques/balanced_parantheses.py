# simple implementation
def balanced(string):
    arr=[]
    if len(string) % 2 != 0:
        return False
    for each in string:
        if each == '[' or each == '{' or each == '(':
            arr.append(each)
        elif each == ']' or each == '}' or each == ')':
            if len(arr)==0:
                return False
            end = arr.pop()
            if each == ']' and end != '[':
                return False
            if each == ')' and end != '(':
                return False
            if each == '}' and end != '{':
                return False
    if len(arr) == 0:
        return True
    else:
        return False


# set implementation, little bit faster than simple
# def balance_check(s):
    
#     # Check is even number of brackets
#     if len(s)%2 != 0:
#         return False
    
#     # Set of opening brackets
#     opening = set('([{') 
    
#     # Matching Pairs
#     matches = set([ ('(',')'), ('[',']'), ('{','}') ]) 
    
#     # Use a list as a "Stack"
#     stack = []
    
#     # Check every parenthesis in string
#     for paren in s:
        
#         # If its an opening, append it to list
#         if paren in opening:
#             stack.append(paren)
        
#         else:
            
#             # Check that there are parentheses in Stack
#             if len(stack) == 0:
#                 return False
            
#             # Check the last open parenthesis
#             last_open = stack.pop()
            
#             # Check if it has a closing match
#             if (last_open,paren) not in matches:
#                 return False
            
#     return len(stack) == 0


balanced('({[(({})])})')
