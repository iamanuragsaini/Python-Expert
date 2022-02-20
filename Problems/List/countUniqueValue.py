# Count unique values inside list

def count_unique_value(list):
    l1 = []
    print("method 1: ")
    tupleCount = set(list)
    print(tupleCount,"\nLength: ", len(tupleCount))
    print("Method 2: ")
    count = 0
    for item in list:
        if item not in l1:
            count += 1           
            l1.append(item)  
    return count
        



list = [2,3,4,5,6,7,3,7,2]
print(count_unique_value(list))