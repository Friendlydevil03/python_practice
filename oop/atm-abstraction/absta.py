from abc import ABC,abstractmethod

class user_show(ABC):

    @abstractmethod
    def card(self,name):
        pass

    @abstractmethod
    def pin(self,pin_number):
        pass

    @abstractmethod
    def withdraw(self,withdraw_cash):
        pass

    @abstractmethod
    def deposit(self,Deposit_cash):
        pass

    @abstractmethod
    def balance_check(self):
        pass


