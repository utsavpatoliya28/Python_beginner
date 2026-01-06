n = int(input("Enter your no.: "))

for i in range(1, n+1):
    if(i==1 or i==n):
        print("* "* n)

    else:
        for i in range(2, n):
            print("* ", end="")
            print(" "* 2*(n-2), end="")
            print("*", end="")
            print("")