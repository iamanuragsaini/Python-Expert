# Find middle three element in string.

def check_element(str):
    size = int(len(str))
    if size%2==1:
        mid = size // 2
    else:
        mid = (size-1)//2
    
    res = str[mid-1:mid+2]
    print(f"Three middle element: {res}")
    return True

str = input("Enter the string: ")
result = check_element(str)
print(result)