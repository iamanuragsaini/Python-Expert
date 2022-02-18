# check element is present or not.
# Using for loop

def checkelement(list, ele):
    for i in list:
        if i==ele:
            return ele

    
list = [2,3,4,5,6,7]
print(f"Your list: {list}")
ele = int(input("enter the element: "))
print(checkelement(list, ele))