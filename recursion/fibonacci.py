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
