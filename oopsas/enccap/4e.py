class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_info(self):
        print(f"Employee Name: {self.name}")

    def get_salary(self):
        return self.__salary

emp = Employee("Kumar", 50000)
emp.show_info()
print(emp.get_salary())
