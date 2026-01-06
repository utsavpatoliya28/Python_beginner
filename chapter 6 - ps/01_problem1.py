a = int(input("Enter your no. 1: "))
b = int(input("Enter your no. 2: "))
c = int(input("Enter your no. 3: "))
d = int(input("Enter your no. 4: "))

if(a>b and a>c and a>d):
    print(" the greatest no. is a: ",a)

elif(b>a and b>c and b>d):
    print(" the greatest no. is b: ",b)

elif(c>a and c>b and c>d):
    print(" the greatest no. is c: ",c)

else:
    print(" the greatest no. is d: ",d)