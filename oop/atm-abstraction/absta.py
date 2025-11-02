from abc import ABC,abstractmethod

class user_show(ABC):

    @abstractmethod
    def card(self,card):
        pass

    # @abstractmethod
    # def pin(self):
    #     pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


    @abstractmethod
    def balance_check(self):
        pass


