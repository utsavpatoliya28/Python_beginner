def max(no1, no2, no3):
    if(no2<no1 and no3<no1):
        print("no1 is the greatest ",no1)
        

    elif(no1<no2 and no3<no2):
        print("no2 is the greatest ",no2)
        

    elif(no1<no3 and no2<no3):
        print("no3 is the greatest ",no3) #if at here we dont use return x then if we write print(max(x)) otherwise it gives us none bcz theres no one value for return
        

max(1,2,3)

a = 1 
b = 2
c = 3
def max(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
print(max(a, b, c))
