from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


"""
##### BAD
class Point:
    def __init__(self, a, b, system: int = CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)
"""


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'x: {self.x} y: {self.y}'

    class PointFactory:
        def new_cartesian_point(self, x: float, y: float) -> 'Point':
            point = Point()
            point.x = x
            point.y = y
            return point

        def new_polar_point(self, rho: float, theta: float) -> 'Point':
            point = Point()
            point.x = rho * cos(theta)
            point.y = rho * sin(theta)
            return point

    factory = PointFactory()


if __name__ == '__main__':
    p = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p)
    print(p2)
