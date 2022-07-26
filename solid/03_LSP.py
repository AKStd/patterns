class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Rectangle width:{self._width}: height:{self._height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def get_area(rc: Rectangle) -> None:
    w = rc.width
    rc.height = 10
    exp = int(w * 10)
    print(f'Got {rc.area}, expect {exp}')


rc = Rectangle(2, 3)
get_area(rc)

sq = Square(5)
get_area(sq)
