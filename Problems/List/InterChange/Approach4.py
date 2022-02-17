# Fourth approach with * operand
# Simple interchange first and last list element.

def interChange(newList):
    first, *middle, end = newList
    newList = end, *middle, first
    return newList

if __name__=='__main__':
    newList = [10,20,30,40,50]
    print(interChange(newList))
