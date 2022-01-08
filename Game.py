# Game-snake water gun
# use random choice function,snake water gun
# swg to choose
# 10 times to run and print the result
import random
flagh=0
flagc=0
drawc=0
a=["snake","water","gun"]
for i in range(10):
    b=random.choice(a)
    c=input("Enter your choice , snake , water or gun:- ")
    if (c=="snake"):
        if(b==c):
            print("Draw")
            drawc = drawc + 1
        elif b=='water':
            print("you wins")
            flagh=flagh+1
        else:
            print("You lose")
            flagc=flagc+1
    elif (c=="water"):
        if(b==c):
            print("Draw")
            drawc=drawc+1
        elif b=='gun':
            print("you wins")
            flagh=flagh+1
        else:
            print("You lose")
            flagc=flagc+1
    elif  (c=="gun"):
        if(b==c):
            print("Draw")
            drawc = drawc + 1
        elif b=='snake':
            print("you wins")
            flagh=flagh+1
        else:
            print("You lose")
            flagc=flagc+1
    else:
        print("Try again")
print(f"Number of times you won out of 10:- {flagh}")
print(f"Number of times you lost out of 10:- {flagc}")
print(f"Number of times draw:- {drawc}")