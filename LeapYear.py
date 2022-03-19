# Check year is leap year or not

 

year = int(input("Enter the Year: "))
print(f"Year name: {year}")
if(year%400==0):
    print("leap year")
elif(year%100==0):
    print("Not leap year")
elif(year%4==0):
    print("leap year")
else:
    print("Not leap year")
