    # run loop till 100 in user Input

while(True):
    userInput = int(input("Enter the number "))
    if(userInput>100):
        print("Successful greater than 100")
        break
    else:
        print(f"Lesser {userInput}")
        continue