g = input("Enter the Gender:\nmale\tfemale\tother\noption: ")
a = int(input("Enter the age: \t"))
if a >= 18:
    print("You are eligable")
    if g == "male" :
        print("you are male")
    elif g == "female":
        print("you are female")
    else:
        print("other")
else:
    print("not eligable")