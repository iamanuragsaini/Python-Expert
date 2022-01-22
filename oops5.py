class Student:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printDetails(self):
        print(f"The name is {self.name} and salary is {self.salary} and the role is {self.role}")

    @classmethod
    def from_str(cls, string):
        param = string.split("-")
        return cls(param[0], param[1], param[2])

    @staticmethod
    def printgood(string):
        print(f"This is good {string}")

class programmer(Student):
    
    def __init__(self, aname, asalary, arole, aprogram):
        self.program = aprogram
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printdet(self):
        print(f"Your name is {self.name} and the programming you know {self.program}")

# anurag = Student("Anurag", 80000, "Data Scientist")
# kamal = Student.from_str("Kamal-40000-CGL")

anurag = programmer("anurag",100,"a",["python","numPy", "Pandas"])
anurag.printdet()
# kamal.printDetails()
# anurag.printDetails()

# anurag.printgood("Anurag")

    


