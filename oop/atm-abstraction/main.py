from atm import ATM
s = ATM("Insert","3333")
s.card("Insert")
s.pin(3333)
s.deposit(100000)
s.withdraw(50000)
s.balance_check()

s = ATM("Insert","1234")
s.card("Insert")
s.pin(1234)
s.deposit(67600)
s.withdraw(6760)
s.balance_check()