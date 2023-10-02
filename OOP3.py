import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return True

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return 'Circle' + super().__str__()[5:-1] + f', radius={self.radius})'

    def __add__(self, other):
        new = super().__add__(other)
        return Circle(self.radius + other.radius, new.x, new.y)

    def __sub__(self, other):
        if self.radius == other.radius:
            x = self.x - other.x
            y = self.y - other.y
            return Point(x, y)
        else:
            new_radius = abs(self.radius - other.radius)
            return Circle(new_radius, self.x, self.y)


circle1 = Circle(15, 4, 2)
circle2 = Circle(20, 6, 8)
result_circle = circle1 - circle2
print(f"Разница окружностей: {result_circle}")

circle1 = Circle(15, 6, 8)
circle2 = Circle(15, 6, 8)
result_circle = circle1 - circle2
print(f"Разница окружностей: {result_circle}")
