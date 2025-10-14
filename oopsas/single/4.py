class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Programmer(Employee):
    def display(self):
        print(f"Programmer: {self.name}, Salary: {self.salary}")

p = Programmer("Rahul", 50000)
p.display()
