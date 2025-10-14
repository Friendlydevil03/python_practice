class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def width(self):
        return f"{self._width:1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("must greater than zero")

    @property
    def height(self):
        return f"{self._height:1f}cm"

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("must greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("deleted")

    @height.deleter
    def height(self):
        del self._height
        print("deleted")

rect = Rectangle(100, 200)

rect.width = 10
rect.height = 20

del rect.width
del rect.height

# print(rect.width, rect.height)

