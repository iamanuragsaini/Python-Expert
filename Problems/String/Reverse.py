# Reverse words in a given String in Python

# Input : str = geeks quiz practice code
# Output : str = code practice quiz geeks

def check_element(string):
    newStr = string.split(' ')
    revStr = ' '.join(newStr[::-1])
    print(revStr)


string = 'geeks quiz practice code'
check_element(string)