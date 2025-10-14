print("welcome to the Grading System")
student_name = input("Enter the student's name: ")

maths_marks = float(input("Enter Maths marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

Total_marks = maths_marks + science_marks + english_marks
Average_marks = Total_marks / 3

print("\n------Results------")
print("Name of the student: ", student_name)
print("Total Marks: ", Total_marks)
print("Average Marks: ", Average_marks)

if Average_marks >= 90:
    Grade = "A+"
elif Average_marks >= 80:
    Grade = "A+"
elif Average_marks >= 70:
    Grade = "B"
elif Average_marks >= 60:
    Grade = "C"
elif Average_marks >= 50:
    Grade = "D"
else:
    Grade = "F"

print("Grade:", Grade)

if Grade == False:
    print("Sorry, you have failed the exam.")
else:
    print("Congratulations, you have passed the exam!")