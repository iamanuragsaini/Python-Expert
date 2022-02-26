string = 'amaama'

mid = int(len(string)/2)

if(len(string)%2==0): 
    first = string[:mid]
    last = string[mid:]
else:
    first = string[:mid]
    last = string[mid+1:]

if(first == last[::-1]):
    print(f"{string} is palindrom")
else:
    print(f"{string} not a palindrom")