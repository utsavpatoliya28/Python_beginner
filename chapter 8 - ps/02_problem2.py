def temp(c):
    if(c < -373):
        print("This temp dosent exist")

    else:
        f = (c*(9/5))+32
        print(f)

a = float(input("Enter your temp: "))

temp(a)

# THis one is not from me                          

def temp(c):
    return (c*(9/5))+32

a = float(input("Enter your temp: "))
print(round(temp(a), 2))        #round figure
print(f"{round(temp(a),2)}")
c = temp(a)
print((f"{round(c, 2)} f"))

#he did f to c but mine, c to f