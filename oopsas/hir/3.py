class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display(self):
        print(f"Owner: {self.owner}, Balance: ₹{self.balance}")

class SavingsAccount(Account):
    def add_interest(self):
        print(f"Interest added to {self.owner}'s savings account.")

class CurrentAccount(Account):
    def overdraft(self):
        print(f"{self.owner} used overdraft facility.")

class FixedDeposit(Account):
    def lock_period(self):
        print(f"{self.owner}'s FD is locked for 5 years.")


s = SavingsAccount("Priya", 50000)
c = CurrentAccount("Rahul", 100000)
f = FixedDeposit("Anita", 200000)

s.display()
s.add_interest()

c.display()
c.overdraft()

f.display()
f.lock_period()
