class Engine:
    def __init__(self,hp,fueltype):
        self.hp = hp
        self.fueltype = fueltype

    def engine_details(self):
        print(f"engine: {self.hp}")
        print(f"fuel: {self.fueltype}")

class Car:
    # E1 =Engine("500","diesel")  #way1
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.E1=Engine("299","disel") #way2

    def car_details(self):
        print(f"car: {self.name}")
        print(f"color: {self.color}")

c1 =Car("BMW","Red")
c1.car_details()
c1.E1.engine_details()