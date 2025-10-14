class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(BankAccount):
    def add_interest(self):
        self.balance += self.balance * 0.05

account = SavingsAccount(1000)
account.add_interest()
print("Balance:", account.balance)
