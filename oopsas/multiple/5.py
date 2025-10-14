class Person:
    def personal_info(self):
        print("Name, Age, Address")

class Subject:
    def teach_subject(self):
        print("Teaching Python")

class Teacher(Person, Subject):
    def show_role(self):
        print("I am a Teacher")

t = Teacher()
t.personal_info()
t.teach_subject()
t.show_role()
