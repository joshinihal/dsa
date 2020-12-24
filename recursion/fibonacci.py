def fib_iteration(n):

#   a=0,b=1
    a,b=0,1
    
    for i in range(n):
        a,b = b,a+b
        
    return a

fib_iteration(5)
