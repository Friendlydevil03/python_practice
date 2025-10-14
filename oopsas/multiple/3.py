class Account:
    def deposit(self, amount):
        print(f"Deposited: {amount}")

class Loan:
    def apply_loan(self, amount):
        print(f"Loan applied: {amount}")

class Customer(Account, Loan):
    def info(self, name):
        print(f"Customer name: {name}")

cust = Customer()
cust.info("Venkatesh")
cust.deposit(5000)
cust.apply_loan(20000)
