class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is being driven.")

class Bike(Vehicle):
    def ride(self):
        print(f"{self.brand} bike is being ridden.")

class Truck(Vehicle):
    def load(self):
        print(f"{self.brand} truck is loading goods.")


# Objects
c1 = Car("Toyota")
b1 = Bike("Yamaha")
t1 = Truck("Tata")

c1.start()
c1.drive()

b1.start()
b1.ride()

t1.start()
t1.load()
