# Second approach with pop
# Simple swap first and second position element in list.

def swapping(list, pos, pos2):
    first = list.pop(pos)
    end = list.pop(pos2-1)
    list.insert(pos, end)
    list.insert(pos2, first)
    return list


list=[2,3,4,5,6,7,8,9]
pos = int(input("enter the position 1: "))
pos2 = int(input("enter the position 2: "))
print(swapping(list,pos, pos2))
