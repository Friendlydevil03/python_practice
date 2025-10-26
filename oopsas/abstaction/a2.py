from a1 import Calculator
class SimpleCalculator(Calculator):
    def add(self,a,b):
        print(f"Addition {a + b}")

    def sub(self,a,b):
        print(f"Subtraction {a - b}")

    def mul(self,a,b):
        print(f"multiplication{a*b}")

    def div(self,a,b):
        print(f"Division of {a/b}")