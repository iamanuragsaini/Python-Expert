# check element is present or not.
# Using count() method

def checkelement(list, ele):
    newSize = list.count(ele)
    return newSize>0
    

    
list = [2,3,4,5,6,7]
print(f"Your list: {list}")
ele = int(input("enter the element: "))
print(checkelement(list, ele))