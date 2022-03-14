#Check if two sets have any elements in common. If yes, display the common elements

def check_element(set1,set2):
    if set1.isdisjoint(set2):
        print("Two sets have no item common.")
    else:
        print("Two sets have common elements")
        print(set1.intersection(set2))
    return True

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

result = check_element(set1,set2)
print(result)