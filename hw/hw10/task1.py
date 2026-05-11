class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

rect = Rectangle(10, 5)
print(f"Площа прямокутника: {rect.get_square()}")