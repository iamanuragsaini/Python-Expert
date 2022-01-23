
# Super or overriding


class Student:
    id = 1  #public
    _name = "Anurag"  #Protected 
    __pwd = 1234   #Private

    def __init__(self, aname,arole):
        self.name = aname
        self.role = arole

class other(Student):
    def __init__(self, aname,arole,asalary):
        super().__init__(aname,arole)
        self.salary = asalary

anurag = other("Anurag","Data Scientist",90000)

print(anurag.name, anurag.role, anurag.salary)
    