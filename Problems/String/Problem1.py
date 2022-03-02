# Find first, middle and last character in string.

# Input : "James"
# Output: Jms

def check_element(str):
    size = int(len(str))
    if size%2==0:
        mid = (size-1) // 2
    else:
        mid = size//2

    print(f"First elm: {str[0]}\nMiddle elm: {str[mid]}\nlast elm: {str[-1]}")    

str = input("Enter the string: ")
# print(check_element(str))
result = check_element(str)
print(result)
