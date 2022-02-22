# Program to get all unique combinations of two lists

''' Input : List_1 = ["a","b"]
List_2 = [1,2]'''
# Output: Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] 

def Unique_combination(list1, list2):
    temp = []
    value = [(x,y) for x in list1 for y in list2]
    return value
            

list1 = ["a","b"]
list2 = [1,2]
print(Unique_combination(list1, list2))