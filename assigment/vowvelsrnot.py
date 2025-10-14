#without argument without return type
def vow():
    a = ['a','e','i','o','u']
    b = input("Enter a vowel: ").lower()
    if b in a :
        print("Is a vowel")
    else:
        print("Is not a vowel")

vow()

# without argument with return type
def vow2():
    a = ['a','e','i','o','u']
    b = input("Enter a vowel: ").lower()
    if b in a :
        return "Is a vowel"
    else:
        return "Is not a vowel"

res=vow2()
print(res)

# with argument without return type
def vow3(b):
    b = b.lower()
    a = ['a','e','i','o','u']
    if b in a :
        print("Is a vowel")
    else:
        print("Is not a vowel")

vow3 (input("Enter a alphabet: "))

# with argument with return type
def vow4(b):
    b = b.lower()
    a = ['a','e','i','o','u']
    if b in a :
        return "is a vowel"
    else:
        return "is a not vowel"

res1= vow4("E")
print(res1)
