
# Try and exception

num1 = input("Enter the first number:- ")
num2 = input("Enter the second number:- ")
try:
    print(f"Your sum is {int(num1)+int(num2)}")
except Exception as e:
    print(e)
print("All ok!")