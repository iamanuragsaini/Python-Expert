# Count occuring of an element in a list
# using simple count() method

def copying(list, num):
    count = list.count(num)
    return count

    

list = [2,3,4,5,6,7,3,7,3]
num = int(input("Enter the element: "))
print(copying(list, num))