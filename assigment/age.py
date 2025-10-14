a = int(input("Enter the age: "))
if a >= 0 and a <= 12:
    print("Child")
elif a >= 13 and a <= 19:
    print("Teenager")
elif a >= 20 and a <= 59:
    print("Adult")
else:
    print("senior citizen")
