def check_balance():
    print("your balance is:",balance)
    print()
def deposit():
    amount = float(input("Enter the amount to deposit:"))
    if amount < 0:
        print("You cannot deposit negative amounts")
    else:
        return amount
    print()

def withdraw():
    amount = float(input("Enter the amount to withdraw:"))
    if balance < amount:
        print("You cannot withdraw less than your balance")
    elif amount <0:
        print("You cannot withdraw less than your balance")
    else:
        return amount
    print()

balance = 0
is_running = True

while is_running :
    print(f"Welcome to the banking app\n1.Checkbalance\n2.Deposit\n3.Withdraw\n4.Exit")
    choice =int(input("Enter your choice: "))
    if choice == 1:
        check_balance()
        print("Your balance is:",balance)
        print()
    elif choice == 2:
        balance += deposit()
        print(f"The amount is deposited")
        print("Your balance is:", balance)
        print()
    elif choice == 3:
        balance += withdraw()
        print("The amount is withdrawn")
        print("Your balance is:", balance)
        print()

    elif choice == 4:
        is_running = False

print("Thank you for using banking app")