# Reduce function

from functools import reduce

lst = [1,2,3,4]
val = reduce(lambda x,y:x+y, lst)
print(val)