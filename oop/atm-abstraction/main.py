from atm import ATM
s = ATM("sri","3333")
s.card("sri")
s.pin(3333)
s.deposit(100000)
s.withdraw(50000)
s.balance_check()

s = ATM("akash","1234")
s.card("akash")
s.pin(1234)
s.deposit(67600)
s.withdraw(500)
s.balance_check()