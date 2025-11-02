from absta import user_show
class ATM2(user_show):
    card_insert = False
    def __init__(self,card_insert,pin_number,balance=0):
        self.card_insert = card_insert
        self.pin_number = pin_number
        self.balance = balance
        self.auth = False
        self.card_insert = card_insert

    def card(self):
        print("*" * 35)
        if  self.card_insert is True:
            self.auth = True
            print(f"      Card Scanned Successfully     ")
            print(f"         Welcome to the ATM        ")
        else:
            print("Please insert the card")
            self.auth = False
        print("*"*35)

    def pin(self, pin_number):
        if self.auth is True:
            str_pin = str(pin_number)
            if str_pin == self.pin_number:
                self.auth = True
            else:
                print("Please enter a valid pin")
                self.auth = False

                
    def deposit(self,deposit_cash):
        if self.auth is True:
            if deposit_cash > 0 :
                print(f"{"-" * 10}Deposit amount{"-" * 10}")
                self.balance += deposit_cash
                print(f"${deposit_cash} deposited")
                print(f"Your Balance is ${self.balance}")
            else:
                print("Enter a valid deposit amount")


    def withdraw(self, withdraw_cash):
        if self.auth is True:
            print(f"{"-"*10}Withraw amount{"-"*10}")
            if withdraw_cash == self.balance :
                print("Bank balance is cannot be $0")
            if withdraw_cash < self.balance:
                self.balance -= withdraw_cash
                print(f"${withdraw_cash} withdraded")
                print(f"Your Balance is ${self.balance}")
            elif withdraw_cash > self.balance:
                print("Insufficient funds")
            print("-" * 35)
    def balance_check(self):
        if self.auth is True:
            print(f"Your bank balance is ${self.balance}")
            print("-"*35)
            print()
