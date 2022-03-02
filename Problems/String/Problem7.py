# Create a mixed string using the following rules.

def check_element(str1, str2):
    str1Length = len(str1)
    str2Length = len(str2)
    length = str1Length if str1Length>str2Length else str2Length
    result = ''
    str2 = str2[::-1]
   
    for i in range(length):
        if i<str1Length:
            result += str1[i]
        elif i < str2Length:
            result += str2[i]
    print(result)


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
print(check_element(str1, str2))