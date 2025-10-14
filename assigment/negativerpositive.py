n = int(input("Enter a value: "))
if n>= -999 and n <= -1:
    print("This is a negative number")
elif n >= 1 and n <= 999:
    print("This is a positive number")
elif n == 0:
    print("This is zero")