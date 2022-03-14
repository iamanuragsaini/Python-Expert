# Update the first set with items that don’t exist in the second set

def check_element(set1,set2):
    newSet = set1.difference(set2)
    return newSet



set1 = {10, 20, 30}
set2 = {20, 40, 50}
result = check_element(set1,set2)
print(result)