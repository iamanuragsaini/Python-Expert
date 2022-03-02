# Count all letters, digits and special symbol from string.

def check_element(str):
    letterCount = 0
    digitCount = 0
    symbolCount = 0
    for item in str:
        if item.isalpha():
            letterCount += 1
        elif item.isdigit():
            digitCount += 1
        else:
            symbolCount += 1
    print(f"Chars = {letterCount}\nDigits = {digitCount}\nSymbol = {symbolCount}")
    return True


str = input("Enter the string: ")
# print(check_element(str))
result = check_element(str)
print(result)