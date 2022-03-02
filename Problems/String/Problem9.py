# Find all occurrences of a substring in string.

# Count india

def check_element(str):
    str = str.lower()
    print(str)
    count = str.count("india")
    return count

str = "Welcome to India. india awesome, isn't it?"
print(check_element(str))
