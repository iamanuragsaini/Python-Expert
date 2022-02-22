# Combination a list in given condition

# Input : test_list = [“geekforgeeks”, [5, 4, 3], “is”, [“best”, “good”, “better”]], K = 3 
# Output : [[‘geekforgeeks’, 5, ‘is’, ‘best’], [‘geekforgeeks’, 4, ‘is’, ‘good’], [‘geekforgeeks’, 3, ‘is’, ‘better’]] 
# Explanation : Inner elements picked and paired with similar indices. 5 -> “best”.

def combination_element(test_list):
    print(f"Original list: {test_list}")
    size = len(test_list)
    res = []
    count = 0
    while count <= size-1:
        temp =[]
        for item in test_list:
            if not isinstance(item, test_list):
                temp.append(item)
            else:
                temp.append(item[count])
        count += 1
        res.append(temp)
        return res
                


test_list = ["geekforgeeks", [5, 4, 3], "is", ["best", "good", "better"]]
print(combination_element(test_list))