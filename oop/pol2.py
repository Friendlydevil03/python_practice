
class Shape:
    def area(self):
        pass

class Circle(Shape):
    name = "Circle"
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)

class Rectangle(Shape):
    name = "Rectangle"
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

class Triangle(Shape):
    name = "Triangle"
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return (self.a*self.b*self.c)/2

class pizza(Circle):
    name = "Pizza"
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping
        self.radius = radius
    # def area(self):
    #     return 3.14*self.topping*self.radius

shapes = [Circle(3),Rectangle(3,6),Triangle(6,6,6),pizza("peppononi",6)]
for a in shapes:
    print(f"Area of {a.name}is {a.area()}")
    # print(a.name)