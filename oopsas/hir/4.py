class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"{self.name} earns ₹{self.salary}")

class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} manages a team.")

class Developer(Employee):
    def write_code(self):
        print(f"{self.name} writes Python code.")

class Designer(Employee):
    def design_ui(self):
        print(f"{self.name} designs user interfaces.")


m = Manager("Suresh", 80000)
d = Developer("Anjali", 70000)
de = Designer("Karan", 65000)

m.show()
m.manage_team()

d.show()
d.write_code()

de.show()
de.design_ui()
