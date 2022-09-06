from abc import ABC


class Shape(ABC):
    def __str__(self) -> str:
        return ""


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def resize(self, factor: float) -> None:
        self.radius *= factor

    def __str__(self) -> str:
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def __str__(self):
        return f"A square of radius {self.side}"


class ColoredShape(Shape):
    def __init__(self, shape: Shape, color: str) -> None:
        if isinstance(shape, ColoredShape):
            raise TypeError("Cannot apply same decorator twice!")
        self.shape = shape
        self.color = color

    def __str__(self) -> str:
        return f"{self.shape} with color {self.color}"


class TransparentShape(Shape):
    def __init__(self, shape: Shape, transparency: float) -> None:
        if isinstance(shape, TransparentShape):
            raise TypeError("Cannot apply same decorator twice!")
        self.shape = shape
        self.transparency = transparency

    def __str__(self) -> str:
        return f"{self.shape} with transparency {self.transparency * 100}%"


if __name__ == "__main__":
    c = Circle(2)
    print(c)
    red_circle = ColoredShape(c, "red")
    print(red_circle)
    red_trans_c = TransparentShape(red_circle, 0.5)
    print(red_trans_c)
