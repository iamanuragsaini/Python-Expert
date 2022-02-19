# Cloning or copying a list
# using slicing

def copying(list):
    newList = list[:]
    return newList

list = [2,3,4,5,6,7]
print(copying(list))