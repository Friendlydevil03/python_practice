#without argument without return type
def check():
    b = int(input("Enter a number: "))
    if b % 2 == 0:
        print("Is a even number")
    else:
        print("Is a odd number")
check()

# without argument with return type
def check2():
    b = int(input("Enter a number: "))
    if b % 2 == 0 :
        return "Is a even number"
    else:
        return "Is a odd number"

res=check2()
print(res)

# with argument without return type
def check3(b):
    if b % 2 == 0:
        print("Is a even number")
    else:
        print("Is a odd number")
check3 (int(input("Enter a number: ")))

# with argument with return type
def check4(b):
    if b % 2 == 0 :
        return "is a even number"
    else:
        return "is a odd number"

res1= check4(int(12))
print(res1)
