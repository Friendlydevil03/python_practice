
#object = A "bundle" of related attributes (variables) and methods (functions)
#       ex . phone,cup,book
#       you need a "class" to create many object
#class = (blueprint) used to design the structure and layout of an object


class Car:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving {self.color} {self.model} ")

    def stop(self):
        print(f"You are stopping {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model} ")