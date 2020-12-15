# Write a recursive function which takes an integer
# and computes the cumulative sum of 0 to that integer

def rec_sum(n):
    if n == 0:
        return 0
    return n + rec_sum(n-1)
    
rec_sum(10)

#-------------------------------------------------

# Given an integer, create a function which returns the sum of all the individual digits in that integer.

def sum_func(n):
    if n<1:
        return 0
    return n%10 + sum_func(int(n/10))
    
sum_func(6577)

#--------------------------------------------------

# Create a function called word_split() which takes in a string phrase and a set list_of_words.
# The function will then determine if it is possible to split the string in a way in which
# words can be made from the list of words.
# You can assume the phrase will only contain words found in the dictionary if it is completely splittable.

def word_split(s,l,output = None):
    if output == None:
        output = []
    
    for word in l:
        if s.startswith(word):
            output.append(word)
            return word_split(s[len(word):],l,output)
    return output
    
word_split('themanran',['the','ran','man'])

