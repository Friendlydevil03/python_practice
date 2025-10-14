class Student:

    #CLASS VARIABLE
    count = 0
    total_gpa = 0
    max_stu = 10

    def __init__(self,name,gpa):
        #INSTANCE VARIABLE
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    #CLASS METHOD
    @classmethod
    def get_count(cls):
        if cls.count == 0:
            return 0
        else:
            return f" {cls.total_gpa / cls.count}"

    @classmethod
    def get_total_gpa(cls):
        return f"Total GPA of student {cls.total_gpa}"

s1 = Student("Alex",3.5)
s2 = Student("lex",2.5)
s3 = Student("ex",3.67)
print(Student.get_count())
print(Student.get_total_gpa())
print(Student.max_stu)
