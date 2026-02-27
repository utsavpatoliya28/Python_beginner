#its just half question 
def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    
    
l = ["Utsav", "Rohan", "Shubham", "Trisha"]

print(rem(l, "Shubham"))

#this one is full que. answer
def rem(l, word):
    n = [] # at here we make new array (list) and last we see this one news output
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Utsav", "Rohan", "Shubham", "an"]

print(rem(l, "an"))