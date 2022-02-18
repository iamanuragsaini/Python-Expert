# First approach with
# Find the length of list

import re


def interChange(List):
    listSize = 0
    for i in list:
        listSize+=1
    return listSize

list = [2,3,4,5,6,7]
print(interChange(list))