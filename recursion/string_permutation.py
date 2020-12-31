# Given a string, write a function that uses recursion to output a list of all the possible permutations of that string.

# For example, given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
def permute(s):
    out=[]
    if len(s)==1:
        out = [s]
    else:
         for i, let in enumerate(s):
                for perm in permute(s[:i] + s[i+1:]):
                    out = out + [let + perm]
    return out
    
permute('abc')
