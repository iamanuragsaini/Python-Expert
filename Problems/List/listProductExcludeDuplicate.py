# print list product have exclude duplicate values

def list_product(list):
    value = set(list)
    count = 1
    for i in value:
        count *= i
    return count

list = [2,3,3,3,4]
print(list_product(list))