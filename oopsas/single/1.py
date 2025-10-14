class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        print("Speed:", self.speed)

class Car(Vehicle):
    def open_door(self):
        print("Door opened")

car1 = Car(120)
car1.show_speed()
car1.open_door()
