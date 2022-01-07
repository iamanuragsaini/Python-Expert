 # Faulty Calculator

print(" 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division")
tupVal = int(input("Enter the operator value "))
val1 = int(input("Enter the first value "))
val2 = int(input("Enter the second value "))

if(tupVal == 1):
    if( val1 == 56 and val2 == 9):
        print("Your answer is 77")
    else:
        print(f"Your answer is {val1+val2}")

elif(tupVal == 2):
        print(f"Your answer is {val1-val2}")

elif(tupVal == 3):
    if( val1 == 45 and val2 == 3):
        print("Your answer is 555")
    else:
        print(f"Your answer is {val1*val2}")

elif(tupVal == 4):
    if( val1 == 56 and val2 == 6):
        print("Your answer is 4")
    else:
        print(f"Your answer is {val1/val2}")
    