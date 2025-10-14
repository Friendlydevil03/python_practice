class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Triangle(Shape):
    def __init__(self, color, is_filled, height, base, ):
        super().__init__(color, is_filled)
        self.height = height
        self.base = base
    def describe(self):
        print(f"area of rectangle is {1/2*self.height * self.base}")
        Shape.describe(self)


class Rectangle(Shape):
    def __init__(self, color, is_filled, height, width, ):
        super().__init__(color, is_filled)
        self.height = height
        self.width = width
    def describe(self):
        print(f"area of rectangle is {self.height * self.width}")
        Shape.describe(self)

class Circle(Shape):
    def __init__(self, color, is_filled, radius, ):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"area of rectangle is {3.14 * self.radius * self.radius}")
        Shape.describe(self)




cir = Circle("red", True, 5)
rec = Rectangle("yellow", False, 5, 4)
tri = Triangle("green", True, 5, 4)

print(cir.__dict__)
print(rec.__dict__)
print(tri.__dict__)
rec.describe()
cir.describe()
tri.describe()


