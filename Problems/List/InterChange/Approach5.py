# Fifth approach with other function like: pop, append and insert.
# Simple interchange first and last list element.

def interChange(newList):
    first = newList.pop(0)
    end = newList.pop(-1)
    newList.append(first)
    newList.insert(0,end)
    return newList

if __name__=='__main__':
    newList = [10,20,30,40,50]
    print(interChange(newList))
