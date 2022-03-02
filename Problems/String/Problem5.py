# Arrange string character i.e. lowerLetter come first

def check_element(str):
    lowerStr = []
    upperStr = []
    for item in str:
        if item.islower():
            lowerStr.append(item)
        else:
            upperStr.append(item)
    return ''.join(lowerStr+upperStr)
    

str = input("Enter the string: ")
print(check_element(str))