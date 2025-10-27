from absta import user_show
class ATM(user_show):
    def __init__(self,name,pin_number,balance=0):
        self.name = name
        self.pin_number = pin_number
        self.balance = balance
        self.auth = False

    def card(self, name):
        if name == self.name:
            self.auth = True
            print(f"Card scanned sucessfully")
            print(f"Welcome to the ATM")
        else:
            print("Please insert the card")
            self.auth = False

    def pin(self, pin_number):
        if self.auth is True:
            str_pin = str(pin_number)
            if str_pin == self.pin_number:
                self.auth = True
            else:
                print("Please enter a valid pin")
                self.auth = False
    def deposit(self,deposit_cash):
        print(f"{"-" * 10}Deposit amount{"-" * 10}")
        if self.auth is True:
            if deposit_cash > 0 :
                self.balance += deposit_cash
                print(f"${deposit_cash} deposited")
            else:
                print("Enter a valid deposit amount")
        print(f"Your Balance is ${self.balance}")
        print("-" * 30)

    def withdraw(self, withdraw_cash):
        print(f"{"-"*10}Withraw amount{"-"*10}")
        if self.auth is True:
            if withdraw_cash == self.balance :
                print("Bank balance is cannot be $0")
            if withdraw_cash < self.balance:
                self.balance -= withdraw_cash
                print(f"${withdraw_cash} withdraded")
            elif withdraw_cash > self.balance:
                print("Insufficient funds")
        print(f"Your Balance is ${self.balance}")
        print("-" * 30)
    def balance_check(self):
        if self.auth is True:
            print(f"Your bank balance is ${self.balance}")
            print()
