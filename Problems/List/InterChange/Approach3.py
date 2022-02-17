# Third approach with tuple
# Simple interchange first and last list element.

def interChange(newList):
    get = newList[0], newList[-1]
    newList[-1], newList[0] = get
    return newList

if __name__=='__main__':
    newList = [10,20,30,40,50]
    print(interChange(newList))
