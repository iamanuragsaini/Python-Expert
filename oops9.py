
# Operator overloading or Dunder Method

class Student:
    id = 1  #public
    _name = "Anurag"  #Protected 
    __pwd = 1234   #Private

    def __init__(self, aname,arole,asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary
    
    def __add__(self,other):
        return self.salary+other.salary

anurag = Student("Anurag","Data Scientist",90000)
kamal = Student("Kamal","CGL",60000)

print(anurag,kamal)

