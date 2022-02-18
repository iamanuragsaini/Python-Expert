# Maximum of two numbers in Python

def maxnumber(num1, num2):
    maxNumber = max(num1, num2)
    return maxNumber

num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))

print(maxnumber(num1, num2))