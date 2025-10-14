o = input("Enter a Operator(+,-,*,/,%,**,//: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if o == '+':
    print(f"The Addition of two Number is {round(a + b)}")
elif o == '-':
    print(f"The Subraction of two Number is {round(a - b)}")
elif o == '*':
    print(f"The Multiplication of two Number is {round(a*b)}")
elif o == '/':
    print(f"The Division of two Number is {round(a / b)}")
elif o == '%':
    print(f"The Modulus of two Number is {round(a % b)}")
elif o == '**':
    print(f"The Power of two Number is {round(a ** b)}")
elif o == '//':
    print(f"The Floor divison of two Number is {round(a // b)}")
else:
    print(f"{o} is invalid operator")

