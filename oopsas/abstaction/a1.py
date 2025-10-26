from abc import ABC, abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

    @abstractmethod
    def sub(self,a,b):
        pass

    @abstractmethod
    def mul(self,a,b):
        pass

    @abstractmethod
    def div(self,a,b):
        pass