# Extract Symmetric Tuples

'''
Input : test_list = [(6, 7), (2, 3), (7, 6)]
Output : {(6, 7)}
'''

testList = [(6,7),(7,6),(2,3)]
temp = set(testList) & {(b,a) for a,b in testList }
print(temp)
result = {(a,b) for a,b in temp if a<b}
print(result)
