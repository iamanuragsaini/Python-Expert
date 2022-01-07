
# Guess the random Number

number = 18
i = 1
while( i<10 ):
    userInput = int(input("Enter the number "))
    if( userInput > 18):
        print("Enter the lower number ")
    elif userInput == 18:
        print("You win")
        break
    else:
        print("Enter the greater number")
    i = i+1
    if i==10:
        print("You exceed your lifeline")
        break
