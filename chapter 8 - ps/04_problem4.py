def sum(n):
    return (n*(n+1))/2

a = float(input("Enter your no.: "))
print(sum(a))

####################
# this one is needed to learn for recursion
'''
sum(1) = 1
sum(2) = 1 + 2
sum(n) = 1 + 2 + 3....+ n-1 + n
sum(n) = sum(n-1) + n

'''
#In recursion if we not mention it start with 1 
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print(sum(100))