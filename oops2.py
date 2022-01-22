class Student:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    def printDetails(self):
        print(f"The name is {self.name} and salary is {self.salary} and the role is {self.role}")

anurag = Student("Anurag", 80000, "Data Scientist")

anurag.printDetails()

    


