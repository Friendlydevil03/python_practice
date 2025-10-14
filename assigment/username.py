User_Name = input("Enter your username: ")

if len(User_Name) > 12:
    print("Your username is too long")
elif " " in User_Name:
    print("Your username should not contain space")
elif not User_Name.isalnum():
    print("Your username should not contain special characters")
else:
    print(f"Your username is {User_Name}")
    print("Your username is valid")