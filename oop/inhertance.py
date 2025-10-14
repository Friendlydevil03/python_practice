class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eat")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def sound(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} is meow")

class Mouse(Animal):
    def sound(self):
        print(f"{self.name} is squcing")

dog = Dog("scooby")
cat = Cat("Tom")
mouse = Mouse("Micky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.sound()
cat.sound()

