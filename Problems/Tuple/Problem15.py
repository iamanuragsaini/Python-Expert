# How to get unique elements in nested tuple

testList = [(3, 4, 5), (4, 5, 7), (1, 4)]
print(f"Original list: {testList}")
result = []
temp=set()
for item in testList:
    for innerItem in item:
        if not innerItem in temp:
            temp.add(innerItem)
            result.append(innerItem)

result.sort(reverse=False)
print(result)