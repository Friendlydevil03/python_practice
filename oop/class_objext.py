
from car import Car

car1 = Car("tesla",2024,"red",False)
# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)
car1.describe()

print()

car2 = Car("mustang",2025,"blue",True)
# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)
car2.describe()
print()

car2.drive()
car1.stop()

