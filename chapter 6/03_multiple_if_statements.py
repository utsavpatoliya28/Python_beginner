a = int(input("Enter your age: "))

#If statment no. 1

if(a%2 == 0):
    print("a is even")

#ENd of if statement no.1

#If statement no.2

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid nagative age")

elif(a==0):
    print("You are entering a 0 which is not a valid age")

else:
    print("You are below the age of consent")

#En d of if statement no. 2