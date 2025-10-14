class Adder:
    def add(self, a, b):
        return a + b

class Multiplier:
    def multiply(self, a, b):
        return a * b

class Calculator(Adder, Multiplier):
    pass

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(5, 3))
