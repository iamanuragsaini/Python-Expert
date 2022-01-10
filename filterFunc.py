# Filter function

def isGreater(n):
    return n>5

l1 = [1,2,3,4,5,6,7,8,9,11]
val = list(filter(isGreater, l1))
print(val)