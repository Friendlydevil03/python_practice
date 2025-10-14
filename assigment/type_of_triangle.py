a = int(input("Enter the first angle:"))
b= int(input("Enter the second angle:"))
c = int(input("Enter the third angle:"))

if a == b == c:
    print("Equilater")
elif a == b  or b == c or a ==c :
    print("Isosceles")
else:
    print("scalene")
