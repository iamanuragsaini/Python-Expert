# Extract element with frequency greater than K

def extract_greater_element(list,k):
    l1 = []
    for item in list:
        freq = list.count(item)
        if freq > k and item not in l1:
            l1.append(item)
    return l1


list = [2,3,4,2,2,2,4,4,4,3,5]
k = int(input("Enter the number: "))
print(extract_greater_element(list,k))