# Cloning or copying a list
# using append() method

def copying(list):
    newList = []
    for i in list:
        newList.append(i)
    return newList

list = [2,3,4,5,6,7]
print(copying(list))