val = input("Enter a value: ")
if val >= "0" and val <= "99999":
    print("The value is a number")
elif val >= "A" and val <= "Z" or val >= "a" and val <= "z":
    print("The value is an Alphabet")
else:
    print("The value is a special character")