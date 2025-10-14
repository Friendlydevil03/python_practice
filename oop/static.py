class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_info(self):
        return f"{self.name}, {self.age}, {self.salary}"

    @staticmethod
    def is_valid(age):
        valid_age = [24,25,26,27,28]
        return age in valid_age

employee1 = Employee("John", 26, 20000)
print(Employee.is_valid(25))