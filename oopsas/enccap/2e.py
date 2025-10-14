
class Car:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10

    def brake(self):
        self.__speed -= 10

    def get_speed(self):
        return self.__speed

car = Car()
car.accelerate()
print(car.get_speed())