# check element is present or not.
# Using tuple

def checkelement(list, ele):
    newVal = set(list)
    print(f"Updated list: {newVal}")
    if ele in newVal:
        return ele
    

    
list = [2,3,4,5,6,7,5,6]
print(f"Your list: {list}")
ele = int(input("enter the element: "))
print(checkelement(list, ele))