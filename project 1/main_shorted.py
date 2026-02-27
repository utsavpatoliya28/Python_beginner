'''
1 for snake 
-1 for water
0 for gun
'''
import random

num = random.choice([0, 1, -1])

computer = num
youstr = input("Enter your choice: ")
youdict = {"s": 1, "W": -1, "g": 0}
reversedict = {1: "Snake", -1: "Water", 0: "Gun"}


you = youdict[youstr]

print(f"You choose {reversedict[you]} \nComputer choose {reversedict[computer]}")

if(computer == you):
    print("Its draw")

else:
    '''
    if(computer == -1 and you == 1): (computer - you)  =  -2
        print("you win!") 

    elif(computer == -1 and you == 0): (computer - you)  = -1
        print("you lose!")

    elif(computer == 1 and you == 0): (computer - you)  = 2
        print("you win!")

    elif(computer == 1 and you == -1): (computer - you)  = 1
        print("you lose!")
        
    elif(computer == 0 and you == -1): (computer - you)  = 1
        print("you win!")

    elif(computer == 0 and you == 1): (computer - you)  = -1
        print("you lose!")

        The below logic is written on the basis of the value of computer - you
    '''
    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose.!")

    elif((computer - you) == 1 or (computer - you) == -2):
        print("You win.!")

    else:
        print("Its draw")