print("It's your grocery shop!")
sum = 0
userName = input("Enter the your name:- ")
print(f"Nice to meet you, {userName}!")
while(True):
        inputUser = input("Enter the fair inputUser:- \n")
        if(inputUser != 'q'):
            print(f"This item of inputUser is {inputUser}\n")
            sum = sum + int(inputUser)
        else:
            print(f"Thanks for coming \n Your total inputUser is {sum}")
    

