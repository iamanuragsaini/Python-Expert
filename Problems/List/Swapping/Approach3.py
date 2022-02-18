# Third approach with tuple
# Simple swap first and second position element in list.


def swapping(list, pos, pos2):
    size = len(list)
    if(pos<size & pos2<size):
        get = list[pos], list[pos2]
        list[pos2], list[pos] = get
        return list
    else:
        return print("Invalid position")
    
list = [2,3,4,5,6,7]
pos = int(input("enter the position 1: "))
pos2 = int(input("enter the position : "))
print(swapping(list, pos, pos2))