# Remove nested records from tuple

'''The original tuple : (1, 5, 7, (4, 6), 10)
Elements after removal of nested records : (1, 5, 7, 10)'''

from tkinter.filedialog import test


testList = (1,5,7,(4,6),8)
print(f"Original tuple: {testList}")
result = tuple()
for i,item in enumerate(testList):
    if not isinstance(item,tuple):
        result += (item,)
        

print(f"Output: {result}")