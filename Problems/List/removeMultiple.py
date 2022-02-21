# Remove multiple element in a list
# Multiples methods

def remove_even_element(list):
    l1 = []
    for i in list:
        if(i%2==0):
            del i
        else:
            l1.append(i)
    return l1   

def remove_odd_element(list):
    for i in list:
        if(i%2==1):
            list.remove(i)            
    return list 

def from_user(list):
    print(f"Given list: {list}")
    num = int(input("Enter the number:"))
    num2 = int(input("Enter the number 2:"))
    value = {num,num2}
    newList = [item for item in list if item not in value]  
    return newList
            

list = [1,2,3,4,5,6,7]
# print("Remove even element",remove_even_element(list))
# print("Remove odd element",remove_odd_element(list))
print(from_user(list))