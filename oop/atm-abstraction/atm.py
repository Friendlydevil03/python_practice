from absta import user_show

class ATM(user_show):
    def __init__(self,name,pin_number,balance=0):
        self.name = name
        self.pin_number = pin_number
        self.balance = balance

    def card(self, name):
        if self.name is None:
            print("Please insert the card")
        else:
            print(self.name)

    def pin(self, pin_number):
        if self.pin_number.isnumeric():
            print("Please enter the amount")
        else:
            print("Please enter a valid pin")

    def deposit(self,deposit_cash):
        if deposit_cash > 0 :
            self.balance += deposit_cash
            print(f"${deposit_cash} deposited")
        else:
            print("Enter a valid deposit amount")

    def withdraw(self, withdraw_cash):
        if withdraw_cash < self.balance:
            self.balance -= withdraw_cash
            print(f"${withdraw_cash} withdraded")
        elif withdraw_cash > self.balance:
            print("Insufficient funds")


    def balance_check(self):
        print(f"Your bank balance is ${self.balance}")