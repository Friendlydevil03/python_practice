n = input("Enter a value: ")
if n >= "A" and n <= "Z":
    print("This is a upper case alphabet")
elif n >= "a" and n <= "z":
    print("This is an lower case alphabet")
elif n >= "-9999" and n <= "0" or n >= "1" and n <= "9999":
    print("This is a number")
else:
    print("This is a special character")
