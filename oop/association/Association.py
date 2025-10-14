"""
Association in Python - Example with Student and Course classes
Association is a relationship where objects have their own lifecycle
and there's no ownership between them.
"""
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []  # List to store associated courses

    def enroll(self, course):
        """Enroll student in a course"""
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            print(f"{self.name} enrolled in {course.name}")

    def drop_course(self, course):
        """Drop a course"""
        if course in self.courses:
            self.courses.remove(course)
            course.remove_student(self)
            print(f"{self.name} dropped {course.name}")

    def list_courses(self):
        """Display all enrolled courses"""
        if self.courses:
            print(f"\n{self.name}'s courses:")
            for course in self.courses:
                print(f"  - {course.name} ({course.code})")
        else:
            print(f"{self.name} is not enrolled in any courses")


class Course:
    def __init__(self, name, code, instructor):
        self.name = name
        self.code = code
        self.instructor = instructor
        self.students = []  # List to store associated students

    def add_student(self, student):
        """Add a student to the course"""
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        """Remove a student from the course"""
        if student in self.students:
            self.students.remove(student)

    def list_students(self):
        """Display all enrolled students"""
        if self.students:
            print(f"\nStudents in {self.name}:")
            for student in self.students:
                print(f"  - {student.name} (ID: {student.student_id})")
        else:
            print(f"No students enrolled in {self.name}")


# Example usage
if __name__ == "__main__":
    # Create students
    s1 = Student("Alice Johnson", "S001")
    s2 = Student("Bob Smith", "S002")
    s3 = Student("Charlie Brown", "S003")

    # Create courses
    c1 = Course("Python Programming", "CS101", "Dr. Williams")
    c2 = Course("Data Structures", "CS201", "Prof. Davis")
    c3 = Course("Web Development", "CS301", "Dr. Martinez")

    # Enroll students in courses (Association)
    s1.enroll(c1)
    s1.enroll(c2)
    s2.enroll(c1)
    s2.enroll(c3)
    s3.enroll(c2)
    s3.enroll(c3)

    # Display course enrollments
    s1.list_courses()
    s2.list_courses()
    s3.list_courses()

    # Display students in courses
    c1.list_students()
    c2.list_students()

    # Drop a course
    print("\n--- Dropping a course ---")
    s1.drop_course(c2)

    # Display updated information
    s1.list_courses()
    c2.list_students()