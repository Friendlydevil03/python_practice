class Vehicle:
    def start(self):
        print("Vehicle started")

class Battery:
    def charge(self):
        print("Battery charging")

class ElectricCar(Vehicle, Battery):
    def drive(self):
        print("Electric car is driving")

tesla = ElectricCar()
tesla.start()
tesla.charge()
tesla.drive()
