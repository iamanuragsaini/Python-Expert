# Extract tuples having K digit elements

'''
Input : test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], K = 2 
Output : [(34, 55), (12, 45), (78,)] 
'''

test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
print("The original list is : " + str(test_list))
K = int(input("Enter the number: "))
res = [sub for sub in test_list if all(len(str(ele)) == K for ele in sub)]
print("The Extracted tuples : " + str(res))
