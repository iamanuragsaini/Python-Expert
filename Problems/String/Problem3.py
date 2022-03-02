# Append new string in the middle of a given string

def check_element(str1, str2):
  
    size = int(len(str1))
    if(size%2==0):
        mid = (size-1)//2
    else:
        mid = size // 2
    x = str1[:mid+1]
    x = x+str2[::]
    x = x+str1[mid:]
    return x

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(check_element(str1, str2))