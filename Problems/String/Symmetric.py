# check string is Symmetric or not
string = 'amaama'

mid = int(len(string)/2)

if(len(string)%2==0): 
    first = string[:mid]
    last = string[mid:]
else:
    first = string[:mid]
    last = string[mid+1:]

if(first == last):
    print(f"{string} is symmetric")
else:
    print(f"{string} not a symmetric")