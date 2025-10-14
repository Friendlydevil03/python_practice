n = int(input("Enter a value: "))
if n >= -9 and  n <= 9:
    print("This is a single digit number")
elif n >= 10 and n <= 99:
    print("This is a two digit number") 
elif n >= 100 and n <= 999:
    print("This is a three digit number")