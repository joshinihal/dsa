# doing manually using dict (2nd fastest soln)
def unique(s):
    seen={}
    for each in s:
        if each in seen:
            return False
        else:
            seen[each] = 1
    return True

# # using set and len function (fastest soln)
# def unique2(s):
#     return len(set(s))==len(s)

# # doing manually using set (slowest of the 3)
# def unique3(s):
#     seen = set()
#     for each in s:
#         if each in seen:
#             return False
#         else:
#             seen.add(each)
#     return True


unique('dghskaHjG8')
