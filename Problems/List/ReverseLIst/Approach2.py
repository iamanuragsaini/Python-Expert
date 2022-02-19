# Reverse the element in the list
# Using slicing method

def reverseelement(list):
    list = list[::-1]
    return list

list = [2,3,4,5,6,7]
print(reverseelement(list))