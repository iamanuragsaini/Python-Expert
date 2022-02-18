# Minimum of two number
# With min() method
def minnumber(num1, num2):
    minNumber = min(num1, num2)
    return minNumber

num1 = int(input("enter the number 1: "))  
num2 = int(input("enter the number 2: "))  
print(minnumber(num1, num2))