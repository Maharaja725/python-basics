# 23. Create a class Polygon with a method to compute perimeter, and derive Triangle and Rectangle classes from it.
class Polygon:
    def __init__(self, *sides):
        self.sides = sides
    def perimeter(self):
        return sum(self.sides)

class Triangle(Polygon):
    pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)

print(Triangle(3,4,5).perimeter())  # Output: 12
print(Rectangle(5,10).perimeter())  # Output: 30
