import sys
from typing import Union


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def resize(self, factor: float):
        self.radius *= factor

    def __str__(self) -> str:
        return f"A circle of radius {self.radius}"


class Square:
    def __init__(self, side: int):
        self.side = side

    def __str__(self) -> str:
        return f"A square with side {self.side}"


class ColoredShape:
    def __init__(self, shape: Union[Square, Circle], color: str):
        self.color = color
        self.shape = shape

    def resize(self, factor: float):
        if isinstance(self.shape, Circle):
            return self.shape.resize(factor)

    # note that a Square doesn't have resize()

    def __str__(self) -> str:
        return f"{self.shape} has the color {self.color}"


# код ниже руками не трогать
shape, size, color = sys.stdin.read().split()

if shape == "c":
    circle = ColoredShape(Circle(int(size)), color)
    result1 = str(circle)
    circle.resize(2)
    result2 = str(circle)

    print(f"{result1} {result2}")

if shape == "s":
    square = ColoredShape(Square(int(size)), color)
    result1 = str(square)
    square.resize(2)
    result2 = str(square)

    print(f"{result1} {result2}")
