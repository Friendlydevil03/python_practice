# Basic Composition Example

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Engine with {self.horsepower}hp started"

    def stop(self):
        return "Engine stopped"


class Wheels:
    def __init__(self, count=4):
        self.count = count

    def rotate(self):
        return f"All {self.count} wheels rotating"


class Car:
    """Car uses composition - it HAS-A engine and wheels"""

    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        # Composition: Car contains Engine and Wheels objects
        self.engine = Engine(horsepower)
        self.wheels = Wheels()

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

    def drive(self):
        return f"{self.make} {self.model} driving. {self.wheels.rotate()}"

    def stop(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"


# Usage
my_car = Car("Toyota", "Camry", 200)
print(my_car.start())
print(my_car.drive())
print(my_car.stop())