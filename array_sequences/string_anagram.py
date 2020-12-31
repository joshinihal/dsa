# string1 is an anagram of string2 if on arranging characters of string1, string2 can be formed.
def anagram(s1,s2):
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    #Edge case check
    if len(s1) != len(s2):
        return False
        
    count = {}
    
    for each in s1:
        if each in count:
            count[each] += 1
        else:
            count[each] = 1
            
    for each in s2:
        if each in count:
            count[each] -= 1
        else:
            count[each] = 1
    
    for k in count:
        if count[k] != 0:
            return False
        
    return True
    
    anagram('Fourth of July','Joyful Fourth')
