a = int(input("Enter marks for subject 1: "))
b = int(input("Enter marks for subject 2: "))
c = int(input("Enter marks for subject 3: "))

# Check for total percentage
total_percentage = ((a+b+c)/300)*100


if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print("the student is passed ",total_percentage)

else:
    print("the student is failed ",total_percentage)

