a = int(input("Enter a units: "))
if a == 100:
    print(f"the total amount of {a} units is {a*2}")
elif 100 < a <= 300:
    print(f"the total amount of {a} units is {a*5}")
elif a > 300:
    print(f"the total amount of {a} units is {a*10}")