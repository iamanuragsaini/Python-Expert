# Map function

l1 = ["1","2","3","4"]
l1 = list(map(int, l1))
print(l1)

def sqrt(x):
    return x*x

def cube(x):
    return x*x*x

l2 = [sqrt,cube]
for i in range(5):
    val = list(map(lambda x:x(i), l2))
    print(val)

l3 = [1,2,3,4,5,6]
val = list(map(lambda x:x*x, l3))
print(val)
