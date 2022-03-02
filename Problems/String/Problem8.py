# String characters balance test

def check_element(str1, str2):
    flag = True
    for item in str1:
        if item in str2:
            continue
        else:
            flag= False
    return flag
        
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(check_element(str1, str2))