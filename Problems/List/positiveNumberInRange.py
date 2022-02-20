# Print all positive number in a range

def positive_number(start,end):
    for num in range(start, end+1):
        if(num>=0):
            print(num)
    return True
  


start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
print(positive_number(start, end))