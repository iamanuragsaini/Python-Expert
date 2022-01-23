
# Data accessing

'''
1. Private
2. Public
3. Protected
'''

class Student:
    id = 1  #public
    _name = "Anurag"  #Protected 
    __pwd = 1234   #Private

    def __init__(self, aname,arole):
        self.name = aname
        self.role = arole

anurag = Student("Anurag", "Data Scientist")

print(anurag._name)
    