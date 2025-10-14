a = int(input("Enter the temperature: "))
if a < 0:
    print("Freezing")
elif a >= 0 and a <= 20:
    print("Cold")
elif a > 20 and a <= 30:
    print("Warm")
else:  
    print("Hot")

