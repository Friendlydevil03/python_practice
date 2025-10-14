class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Cow(Animal):
    def sound(self):
        print("Cow moos")


dog1 = Dog()
cat1 = Cat()
cow1 = Cow()

dog1.sound()
cat1.sound()
cow1.sound()
