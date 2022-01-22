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

anurag = Student("Anurag", 80000, "Data Scientist")
kamal = Student.from_str("Kamal-40000-CGL")

# kamal.printDetails()
# anurag.printDetails()

anurag.printgood("Anurag")

    


