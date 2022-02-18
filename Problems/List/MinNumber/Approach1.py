# Minimum of two number
# With if else
def minnumber(num1, num2):
    if num2>num1:
        return num1
    else:
        return num2

num1 = int(input("enter the number 1: "))  
num2 = int(input("enter the number 2: "))  
print(minnumber(num1, num2))