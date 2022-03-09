# Python program to Sort Tuples by their Maximum element

'''
The original list is : [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
Sorted Tuples : [(19, 4, 5, 3), (4, 5, 5, 7), (1, 3, 7, 4), (1, 2)]
'''

testList = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
print(f"Original list: {testList}")

testList.sort(reverse=True)
print(testList)