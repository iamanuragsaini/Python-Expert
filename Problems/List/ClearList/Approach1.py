# Clear all element in the list
# using del 

def clearlist(list):
    del list[:]
    return True
   

list = [2,3,4,5,6,7]
print(f" Before deletion: {list}")
print(clearlist(list))
print(f" After deletion: {list}")

