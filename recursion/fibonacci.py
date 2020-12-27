def fib_iteration(n):

#   a=0,b=1
    a,b=0,1
    
    for i in range(n):
        a,b = b,a+b
        
    return a

fib_iteration(5)


def fib_recursion(n):
    if n == 0 or n==1:
        return n
    else:
        return fib_recursion(n-1)+fib_recursion(n-2)
    
fib_recursion(5)


     
# memoization or dynamic programming 
# (by remembering the solution in cache)

def fib_dynamic(n, cache):
#     take n and cache
# check for base conditions
    if n == 0 or n==1:
        return n
#     if cache dict has an element with 'n' key,
#     n was peviously encountered and it's value is
#     stored in cache
    if n in cache and cache[n] != None:
        return cache[n]
    else:
#         store value in cache at nth key
        cache[n] = fib_dynamic(n-1,cache)+fib_dynamic(n-2,cache)
#     return after storing
    return cache[n]

# pass n and empty dictionary for cache 
fib_dynamic(5,{})
