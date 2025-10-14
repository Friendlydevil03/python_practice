# class variable = share among all the instant of a class
#define outside the constructor
# allow to share data among all object from class

class Student:

    class_year = 2025
    num_stud = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_stud += 1

student1 = Student("John",20)
student2 = Student("kalgo",21)
student3 = Student("dragon",31)
student4 = Student("kero",24)

print(student1.name,student1.age)
print(student2.name,student2.age)

print(f"My graduating class of {Student.class_year} has {Student.num_stud} studenst")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

