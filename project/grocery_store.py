items = ('banana','apple','orange','bread','milk','eggs')
prices = (50,120,50,35,25,60)

cart = []
print("--------- store ---------")
for i in range (len(items)):
    print(f"{i+1}. {items[i]} - $ {prices[i]} ")

while True:
    choice = input("Enter items to the cart or enter ''done'' to finish: ")
    if choice.lower() == 'done':
        break
    elif choice.isdigit() and 1 <= int(choice) <= len(items):
        cart.append(int(choice)-1)
        print(f"{items[int(choice)-1]} added to your cart")
    else:
        print("Invalid input")

total = 0
print("\n ======= Your Cart ======")
for index in cart:
    print(f"{items[index]} $ {prices[index]}")
    total += prices[index]

print(f"Total: ${total}")
print("Thanks for Shopping")
