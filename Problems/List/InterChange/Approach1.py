#simple interchange first and last list element.

def interChange(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    return newList

if __name__=='__main__':
    newList = [10,20,30,40,50]
    print(interChange(newList))
