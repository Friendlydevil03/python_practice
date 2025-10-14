class Animal:
    def __init__(self,name):
       self.name = name
    def eat(self):
        print(f"{self.name} is eat")

    def sleep(self):
        print(f"{self.name} is sleep")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is flee")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hwak(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Bug")
hwak = Hwak("Tony")
fish = Fish("Nemo")

rabbit.flee()
hwak.hunt()
fish.hunt()
fish.flee()
rabbit.eat()
rabbit.sleep()
