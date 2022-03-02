# Create new string made of first, middle and last character of each string.

def check_element(str1, str2):
    midFirst = len(str1)//2
    midSecond = len(str2)//2
    firstString = str1[0] + str2[0]
    middleString = str1[midFirst] + str2[midSecond]
    lastString = str1[-1] + str2[-1]
    return firstString+middleString+lastString 

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(check_element(str1, str2))