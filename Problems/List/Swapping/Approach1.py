# First approach with comma
# Simple swap first and second position element in list.

def swapping(list, pos, pos2):
    list[pos-1], list[pos2-1] = list[pos2-1], list[pos-1]
    return list


list=[2,3,4,5,6,7,8,9]
pos = int(input("enter the position 1: "))
pos2 = int(input("enter the position 2: "))
print(swapping(list,pos, pos2))
