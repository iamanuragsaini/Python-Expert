# Maximum of two numbers in Python
# using If else method

def maxnumber(num1, num2):
    if(num1>num2):
        print(num1)
    else:
        print(num2)
    return True

num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))

print(maxnumber(num1, num2))