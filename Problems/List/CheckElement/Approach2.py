# check element is present or not.
# Using in

def checkelement(list, ele):
    if ele in list:
        return ele
    else:
        return False

    
list = [2,3,4,5,6,7]
print(f"Your list: {list}")
ele = int(input("enter the element: "))
print(checkelement(list, ele))