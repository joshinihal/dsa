# Factorials:
# 4! = 4*3*2*1 = 4*(3*2*1) = 4*(3!) therefore, n! = n*(n-1)!
# also, if n=0, n!=1

def fact(n):
    # base case
    if n==0:
        return 1
    else:
        return n*fact(n-1)

fact(5)