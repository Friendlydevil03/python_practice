from absta import user_show
class ATM(user_show):
    def __init__(self,balance=0):
        self.balance = balance
        self.auth = False
        self.card_insert = False
        self.pin_no = {1111:"sana", 2222:"sam", 3333:"shaik", 4444:"val", 5555:"phn"}
    def card(self,card):
        self.card_insert = card
        if  self.card_insert is True:
            self.auth = True
            print(f"      Card Scanned Successfully     ")
            print(f"         Welcome to the ATM        ")
        else:
            print("Please insert the card")
            self.auth = False
        attempt = 3
        while attempt > 0:
            if self.auth:
                pin_number=input("Enter your pin number: ")
                pin_number = int(pin_number)
                if pin_number in self.pin_no.keys():
                        self.auth = True
                        self.main_menu()
                else:
                    print("incorrect pin number")
                    print(f"Remaining attempts {attempt-1} ")
                    attempt -=1
    def main_menu(self):
        while self.auth:
                print(f"Welcome to the banking app \n1.Check_balance\n2.Deposit\n3.Withdraw\n4.Exit")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.balance_check()
                elif choice == 2:
                    self.deposit()
                elif choice == 3:
                    self.withdraw()
                elif choice == 4:
                    self.auth = False
                    break
                else:
                    print("    Enter a valid choice!!")
                    print()
    def deposit(self):
        if self.auth:
            deposit_cash = int(input("Enter your deposit amount: "))
            if deposit_cash > 0 :
                self.balance += deposit_cash
                print(f"${deposit_cash} deposited")
                print(f"Your Balance is ${self.balance}")
                back = input("Do you want to continue (y/n)?: ")
                back = back.lower()
                if back == "y":
                    self.main_menu()
                elif back == "n":
                    print("Thank you!! Please remove your card")
                    self.auth=False
            else:
                print("Enter a valid deposit amount")
                print("-" * 35)
    def withdraw(self):
        if self.auth:
                withdraw_cash = int(input("Enter your withdraw amount: "))
                while True:
                    if withdraw_cash == self.balance :
                        print("Bank balance cannot be $0")
                        break
                    elif withdraw_cash<0:
                        print("Amount Cannot Be Negative")
                        print()
                        break
                    elif withdraw_cash==0:
                        print("Amount Cannot be Zero")
                        print()
                        break
                    elif withdraw_cash < self.balance:
                        self.balance -= withdraw_cash
                        print(f"${withdraw_cash} withdraw")
                        print(f"Your Balance is ${self.balance}")
                        back = input("Do you want to continue (y/n)?: ")
                        back = back.lower()
                        if back == "y":
                            self.main_menu()
                        elif back == "n":
                            self.auth = False
                            print("please remove your card")
                            break
                        elif withdraw_cash > self.balance:
                            print("Insufficient funds")
                            break
                        print("-" * 35)
    def balance_check(self):
        if self.auth:
            while True:
                print(f"Your bank balance is ${self.balance}")
                back = input("Do you want to continue (y/n)?: ")
                back = back.lower()
                if back == "y":
                    self.main_menu()
                elif back == "n":
                    print("-" * 35)
                    print()
                    break