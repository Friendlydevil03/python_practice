class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(SchoolMember):
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(SchoolMember):
    def teach(self):
        print(f"{self.name} is teaching.")

class Staff(SchoolMember):
    def manage(self):
        print(f"{self.name} is managing school operations.")


s1 = Student("Ravi", 16)
t1 = Teacher("Meena", 35)
st1 = Staff("Kumar", 40)

s1.info()
s1.study()

t1.info()
t1.teach()

st1.info()
st1.manage()
