students = {}
def add_students():
    name = input("Enter student's name: ").strip().title()
    marks = list(map(int,input("Enter marks for 5 subjects separated by a space: ").split()))
    students[name] = marks
    print(f"{name} added sucessfully!\n")

def calculate_grade(marks):
    avg=sum(marks)/len(marks)
    if avg > 90:
        return "A+"
    elif avg > 80:
        return "A"
    elif avg > 70:
        return "B"
    elif avg > 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "Fail"
def show_report(name,marks):
    total = sum(marks)
    avg = total / len(marks)
    grade = calculate_grade(marks)
    print("\n-------report card-------\n")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {avg}")
    print(f"Grade: {grade}")
    print(f"Higest:{max(marks)}")
    print(f"Lowest:{min(marks)}")
    print("------------------------------\n")

def show_all():
    if not students:
        print("No students\n")
        return
    for name, marks in students.items():
        show_report(name,marks)

def search_student():
    name = input("Enter student's name: ").strip().title()
    if name in students:
        show_report(name,students[name])
    else:
        print("Student not found\n")

def main():
    while True:
        print("Student Report Card System")
        print("1. Add Student")
        print("2. Show all report cards")
        print("3. Search Student")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_students()
        elif choice == 2:
            show_all()
        elif choice == 3:
            search_student()
        elif choice == 4:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice\n")

main()